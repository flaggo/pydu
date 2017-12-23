

BYTE_UNITS = ('B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB')


class Bytes(object):
    """
    Supply several methods dealing with bytes.
    """
    def __init__(self, bytes):
        self.bytes = bytes

    def convert(self, unit=None, multiple=1024):
        """
        Convert bytes with given ``unit``.
        If `unit` is None, convert bytes with suitable unit.
        Convert `multiple` is default to be 1024.
        """
        step = 0
        if not unit:
            while self.bytes >= multiple and step < len(BYTE_UNITS) - 1:
                self.bytes /= multiple
                step += 1
            unit = BYTE_UNITS[step]

        else:  # convert to specific unit
            index_of_unit = BYTE_UNITS.index(unit)
            while len(BYTE_UNITS) - 1 > step and index_of_unit != step:
                self.bytes /= multiple
                step += 1
        return self.bytes, unit
