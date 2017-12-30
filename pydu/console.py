import sys
import shutil

from .platform import WINDOWS, POSIX


if hasattr(shutil, 'get_terminal_size'):
    # Actually (80, 25) is the default size used by many terminal emulators
    def console_size(fallback=(80, 25)):
        return shutil.get_terminal_size(fallback=fallback)
else:
    # http://bitbucket.org/techtonik/python-pager
    def console_size(fallback=(80, 25)):
        """
        For Windows, return (width, height) of available window area, fallback
        if no console is allocated.
        For POSIX system, return (width, height) of console terminal, fallback
        on IOError, i.e. when no console is allocated.
        For other system, return fallback.
        Fallback defaults to (80, 25) which is the default size used by many
        terminal emulators.
        """

        if WINDOWS:
            STD_OUTPUT_HANDLE = -11

            # get console handle
            from ctypes import windll, Structure, byref
            try:
                from ctypes.wintypes import SHORT, WORD, DWORD
            except ImportError:
                from ctypes import (
                    c_short as SHORT, c_ushort as WORD, c_ulong as DWORD)
            console_handle = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

            # CONSOLE_SCREEN_BUFFER_INFO Structure
            class COORD(Structure):
                _fields_ = [('X', SHORT), ('Y', SHORT)]

            class SMALL_RECT(Structure):
                _fields_ = [('Left', SHORT), ('Top', SHORT),
                            ('Right', SHORT), ('Bottom', SHORT)]

            class CONSOLE_SCREEN_BUFFER_INFO(Structure):
                _fields_ = [('dwSize', COORD),
                            ('dwCursorPosition', COORD),
                            ('wAttributes', WORD),
                            ('srWindow', SMALL_RECT),
                            ('dwMaximumWindowSize', DWORD)]

            sbi = CONSOLE_SCREEN_BUFFER_INFO()
            ret = windll.kernel32.GetConsoleScreenBufferInfo(
                console_handle, byref(sbi))
            if ret == 0:
                return fallback
            return ((sbi.srWindow.Right - sbi.srWindow.Left + 1) or fallback[0],
                    (sbi.srWindow.Bottom - sbi.srWindow.Top + 1) or fallback[1])

        elif POSIX:
            # http://www.kernel.org/doc/man-pages/online/pages/man4/tty_ioctl.4.html
            from fcntl import ioctl
            from termios import TIOCGWINSZ
            from array import array

            """
            struct winsize {
                unsigned short ws_row;
                unsigned short ws_col;
                unsigned short ws_xpixel;   /* unused */
                unsigned short ws_ypixel;   /* unused */
            };
            """
            winsize = array("H", [0] * 4)
            try:
                ioctl(sys.stdout.fileno(), TIOCGWINSZ, winsize)
            except IOError:
                # for example IOError: [Errno 25] Inappropriate ioctl for device
                # when output is redirected
                pass
            return winsize[1] or fallback[0], winsize[0] or fallback[1]

        return fallback
