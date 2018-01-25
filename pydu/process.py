try:
    import psutil
except ImportError:
    raise ImportError('Need to pip install psutil if you use pydu.process')


def get_processes_by_path(path):
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
            if path not in using_path:
                continue
            pinfos.append({
                'pid': pinfo['pid'],
                'name': pinfo['name'],
                'cmdline': pinfo['exe']
            })
    return pinfos
