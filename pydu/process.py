try:
    import psutil
except ImportError:
    raise ImportError('Need to pip install psutil if you use pydu.process')

from .path import is_super_path


def get_processes_by_path(path):
    """
    Get processes which are running on given path or sub path of given path.
    """
    pinfos = []
    for proc in psutil.process_iter():
        pinfo = proc.as_dict(attrs=['pid', 'name', 'exe', 'cwd', 'open_files'])

        using_paths = []
        if pinfo['exe']:
            using_paths.append(pinfo['exe'])
        if pinfo['cwd']:
            using_paths.append(pinfo['cwd'])
        if pinfo['open_files']:
            using_paths.extend(pinfo['open_files'])

        for using_path in using_paths:
            if is_super_path(path, using_path):
                continue
            pinfos.append({
                'pid': pinfo['pid'],
                'name': pinfo['name'],
                'cmdline': pinfo['exe']
            })
    return pinfos
