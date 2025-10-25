import re
import time
import random

def get_cookie(email, password, token=None):  # Thêm param token từ QuanHau
    """
    Cải thiện: Tránh garbled bằng identity encoding, rotate UA, dùng token nếu có,
    retry 3 lần, fallback content nếu text fail.
    """
    session = requests.Session()
    
    # Rotate User-Agents (thêm nhiều hơn)
    user_agents = [
        'Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        'Mozilla/5.0 (Linux; Android 9; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    ]
    
    max_retries = 3
    for retry in range(max_retries):
        ua = random.choice(user_agents)
        headers = {
            'User-Agent': ua,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'identity',  # FIX: Tránh gzip garbled
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': 'no-cache',
            'Pragma': 'no-cache',  # Thêm để clear cache
            'Referer': 'https://m.facebook.com/',  # FIX: Thêm referer
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1'
        }
        session.headers.update(headers)
        session.cookies.clear()  # Clear cookies mỗi retry
        
        try:
            # Nếu có token từ reg, dùng để auth trực tiếp (tránh login)
            if token:
                print(f'{vua}{vang}[+] Dùng token từ registration để lấy cookie...')
                # Set token as cookie hoặc Graph API call (nếu có access_token)
                session.headers['Authorization'] = f'Bearer {token}'
                home_resp = session.get('https://m.facebook.com/home.php', timeout=10)
                if 'c_user' in session.cookies:
                    # Extract cookies
                    cookies_dict = dict(session.cookies)
                    important_cookies = {k: v for k, v in cookies_dict.items() if k in ['c_user', 'xs', 'datr', 'fr', 'sb']}
                    cookie_str = '; '.join([f'{k}={v}' for k, v in important_cookies.items()])
                    print(f'{vua}{xanh_la}[√] Cookie từ token: {cookie_str}')
                    return cookie_str
                else:
                    print(f'{vua}{do}[×] Token không valid cho session.')
            
            # Fallback: Login thủ công
            time.sleep(random.uniform(2, 5))  # Delay dài hơn
            print(f'{vua}{vang}[+] Đang warm up homepage (retry {retry+1}/{max_retries})...')
            home_url = 'https://m.facebook.com'
            home_resp = session.get(home_url, timeout=10)
            
            # Kiểm tra garbled: Nếu text ngắn hoặc binary-like, fail
            if len(home_resp.text) < 1000 or not home_resp.text.startswith('<!DOCTYPE'):
                print(f'{vua}{do}[×] Garbled response tại home (len: {len(home_resp.text)}). Thử proxy.')
                continue
            
            login_url = 'https://m.facebook.com/login.php'
            login_resp = session.get(login_url, timeout=10)
            
            if 'checkpoint' in login_resp.text.lower() or len(login_resp.text) < 1000:
                print(f'{vua}{do}[×] Checkpoint hoặc garbled tại login.')
                continue
            
            # Parse fields (cải thiện regex)
            lsd_match = re.search(r'name=["\']lsd["\'] value=["\']([^"\']+)["\']', login_resp.text)
            jazoest_match = re.search(r'name=["\']jazoest["\'] value=["\']([^"\']+)["\']', login_resp.text)
            lsd = lsd_match.group(1) if lsd_match else ''
            jazoest = jazoest_match.group(1) if jazoest_match else ''
            
            if not lsd or not jazoest:
                print(f'{vua}{do}[×] Không parse được lsd/jazoest.')
                continue
            
            # Post login
            login_data = {
                'lsd': lsd,
                'jazoest': jazoest,
                'm_ts': str(int(time.time())),
                'li': 'KXg6H2I3yQ9t0a1',
                'try_number': '0',
                'unrecognized_tries': '0',
                'email': email,
                'pass': password,
                'login': 'Log In',
                'bi_xrwh': '0'  # Thêm param chống bot nếu cần
            }
            
            time.sleep(random.uniform(1, 3))
            post_response = session.post(login_url, data=login_data, allow_redirects=True, timeout=10)  # Cho phép redirect
            
            # Fallback: Nếu text garbled, thử content
            if not post_response.text or len(post_response.text) < 500:
                post_text = post_response.content.decode('utf-8', errors='ignore')
                print(f'{vua}{do}[×] Text garbled, fallback content len: {len(post_text)}')
                if 'checkpoint' in post_text.lower():
                    print(f'{vua}{do}[×] Checkpoint detected in fallback.')
                    continue
            else:
                post_text = post_response.text
            
            if 'checkpoint' in post_text.lower():
                print(f'{vua}{do}[×] Checkpoint sau post: {email}')
                continue
            
            if post_response.status_code in [200, 302] and 'c_user' in session.cookies:
                print(f'{vua}{xanh_la}[√] Login OK (retry {retry+1}) cho: {email}')
                
                # Warm up home để stable session
                time.sleep(random.uniform(2, 4))
                homepage_resp = session.get('https://m.facebook.com/home.php', timeout=10)
                if 'checkpoint' in homepage_resp.text.lower():
                    print(f'{vua}{do}[×] Checkpoint sau warm up.')
                    continue
                
                # Parse fb_dtsg
                fb_dtsg_match = re.search(r'name=["\']fb_dtsg["\'] value=["\']([^"\']+)["\']', homepage_resp.text)
                fb_dtsg = fb_dtsg_match.group(1) if fb_dtsg_match else ''
                print(f'{vua}{vang}[+] fb_dtsg: {fb_dtsg[:20]}...')
                
                # Cookies
                cookies_dict = dict(session.cookies)
                important_cookies = {k: v for k, v in cookies_dict.items() if k in ['c_user', 'xs', 'datr', 'fr', 'sb', 'locale', 'm_pixel_ratio', 'act']}
                cookie_str = '; '.join([f'{k}={v}' for k, v in important_cookies.items()])
                
                print(f'{vua}{xanh_la}[+] Cookie: {cookie_str}')
                return cookie_str
            else:
                print(f'{vua}{do}[×] Post fail (status: {post_response.status_code}, no c_user). Retry {retry+1}/{max_retries}')
                time.sleep(5)  # Delay giữa retry
        
    print(f'{vua}{do}[×] Tất cả retry fail cho {email}. Thử proxy hoặc login thủ công.')
    return None
# Thêm phần lấy cookie...
print(f'{vua}{vang}[+] Đang lấy cookie...')
cookie = get_cookie(email, password, token)  # Truyền token
if cookie:
    print(f'{vua}{xanh_la}[√] Cookie lưu: {email}')
    # Lưu file: with open(f'cookie_{email.split("@")[0]}.txt', 'w') as f: f.write(cookie)
else:
    print(f'{vua}{do}[×] Fail cookie: {email}')
