# 🎭 Gain Stealer - Advanced Windows Information Stealer
📌 Features
🔐 Credential Stealer

    Browser Passwords: Chrome, Edge, Brave, Firefox passwords

    Browser Cookies: All browser cookies + session hijacking

    Discord Tokens: Desktop + Browser tokens

    Crypto Wallets: Exodus, Atomic, MetaMask, Trust Wallet, Electrum

    Telegram Sessions: tdata folder theft

💻 System Information

    Computer name, username, Windows version

    CPU, RAM, disk information

    Installed software list

    Antivirus detection

    IP address and MAC address

📁 File Grabber

    .txt, .doc, .pdf, .xlsx, .csv, .sql, .env files

    Desktop, Documents, Downloads folders

    Auto ZIP creation with password (1234)

🛡️ Anti-Analysis & Evasion

    VM Detection: VMware, VirtualBox, Hyper-V detection

    Sandbox Detection: Low uptime, few CPU cores check

    Startup Delay: Sandbox timeout bypass

    Mutex Check: Single instance execution

    Admin Elevation: Automatic admin privileges

    Persistence: Registry + Startup folder


# 🚀 Installation & Usage
open cmd and type
pip install -r requirements.txt
if not works use this
python -m pip install -r requirements.txt

used packages:
pyinstaller
requests
pycryptodome
browser_cookie3
pywin32
psutil
pyperclip

2. Builder Usage

    Run build.exe

    Enter Discord webhook URL

    Select desired features

    Configure anti-analysis settings

    Set obfuscation options

    Click Build Python Script or Build EXE

3. Modular Structure

Builder downloads modules from raw GitHub URLs:

    imports.py - Required imports

    config.py - Webhook and configuration

    anti_analysis.py - Anti-analysis functions

    password_stealer.py - Password stealing

    cookie_stealer.py - Cookie stealing

    token_stealer.py - Discord token stealing

    data_handler.py - Data packaging and sending

    main.py - Main execution

⚙️ Configuration
Discord Webhook

    Create channel in Discord server

    Channel settings → Integrations → Webhooks

    Create new webhook

    Paste URL into builder

Customization

    Raw URLs: Can be changed in builder

    Output name: Customizable

    Features: Each can be toggled individually

📦 Output
Python Script

    .py executable script

    Obfuscation options applied

Executable (EXE)

    Single file, portable

    Windowed mode (invisible)

    Small size with UPX compression

    Automatic admin elevation

🛡️ Security Features
Anti-Detection

    Signature Avoidance: Unique builds each time

    Resource Obfuscation: No strings in plaintext

    Process Injection: Can inject into legitimate processes

    Timing Attacks: Delays to avoid sandbox detection

Stealth Features

    Silent Execution: No console window

    Clean Traces: Removes temp files after execution

    Legitimate Icon: Can use custom icons (Word, PDF, etc.)

    File Binding: Can bind with legitimate files

🔧 Technical Details
Data Collection Process

    Initial Checks: VM/sandbox detection, mutex check

    Privilege Escalation: Auto-admin if not elevated

    Delay Execution: Configurable startup delay

    Data Harvesting: Parallel collection of all enabled features

    Packaging: JSON files + grabbed files → ZIP with password

    Exfiltration: Discord webhook (embed + file attachment)

    Cleanup: Self-destruct and trace removal

Supported Browsers

    Google Chrome (All versions)

    Microsoft Edge

    Brave Browser

    Mozilla Firefox

    Opera/Opera GX

Supported Crypto Wallets

    Exodus

    Atomic Wallet

    MetaMask (Browser extension)

    Trust Wallet

    Electrum

    Coinomi

    Jaxx

    Binance

⚠️ Legal Disclaimer

FOR EDUCATIONAL AND RESEARCH PURPOSES ONLY

This tool is designed for:

    Security research and education

    Penetration testing (with proper authorization)

    Security awareness training

    Academic study of malware techniques

ILLEGAL USE IS STRICTLY PROHIBITED

The developers assume no liability and are not responsible for any misuse or damage caused by this program. Use only on systems you own or have explicit permission to test.
🐛 Troubleshooting
Common Issues

    "PyInstaller not found"

pip install pyinstaller

"Missing dependencies"

pip install requests pycryptodome browser_cookie3 pywin32 psutil

    "Webhook not sending"

        Check Discord webhook URL

        Verify internet connection

        Check firewall/antivirus blocking

    "EXE detected as virus"

        Disable real-time protection temporarily

        Use different obfuscation settings

        Add to antivirus exclusions

Debug Mode

Run the Python script directly to see errors:


python gain.py

📧 Contact

GitHub: exsarorrayzer
For educational inquiries only

⚠️ WARNING: This software is for legitimate security testing only. Unauthorized access to computer systems is illegal. Always obtain proper authorization before testing any system.
