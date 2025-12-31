def getsysteminfo():
    info = {}
    
    try:
        info['computer_name'] = os.environ.get('COMPUTERNAME', 'Unknown')
        info['username'] = os.environ.get('USERNAME', 'Unknown')
        
        try:
            import platform
            info['windows_version'] = platform.version()
            info['architecture'] = platform.architecture()[0]
            info['processor'] = platform.processor()
        except:
            pass
        
        info['cpu_cores'] = psutil.cpu_count()
        info['ram_gb'] = round(psutil.virtual_memory().total / (1024**3), 2)
        
        try:
            import socket
            info['local_ip'] = socket.gethostbyname(socket.gethostname())
        except:
            pass
        
        try:
            import uuid
            info['mac_address'] = ':'.join(re.findall('..', uuid.getnode().hex))
        except:
            pass
        
    except Exception as e:
        info['error'] = str(e)
    
    return info
