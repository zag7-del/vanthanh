import requests
import random
import string
import hashlib
import os
import re
import time

trang = "\033[1;37m\033[1m"
xanh_la = "\033[1;32m\033[1m"
xanh_duong = "\033[1;34m\033[1m"
xanhnhat = '\033[1m\033[38;5;51m'
do = "\033[1;31m\033[1m\033[1m"
xam = '\033[1;30m\033[1m'
vang = "\033[1;33m\033[1m"
tim = "\033[1;35m\033[1m"
hongnhat = "#FFC0CB"
kt_code = "</>"
dac_biet = "\033[32;5;245m\033[1m\033[38;5;39m"
vua = "\033[1;31m\033[1m[\033[1;37m\033[1m=.=\033[1;31m\033[1m\033[1m] \033[1;37m\033[1m=> \033[1;32m\033[1m"

import os
try:
    from faker import Faker
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import pad
    import requests
except ImportError:
    os.system('pip install Faker')
    os.system('pip install requests')
    os.system('pip install pycryptodome')
    
    
# Import lại sau khi cài đặt
from faker import Faker
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import requests

banner = """
\033[1;33m╔═══════════════════════════════════════════════╗
\033[1;33m║\033[1;35m██╗░░██╗██████╗██████═╗░██╗░░░░██░░░░██╗██████╗\033[1;33m║
\033[1;33m║\033[1;33m██║░░██║██░░░░║██░░░██╝░██║░░░░░██░░██╔╝██░░░░║\033[1;33m║
\033[1;33m║\033[1;39m███████║██████║██████╚╗░██║░░░░░░████╔╝░██████║\033[1;33m║
\033[1;33m║\033[1;36m██╔══██║██░░░░║██╔══██╚╗██║░░░░░░░██╔╝░░░░░░██║\033[1;33m║
\033[1;33m║\033[1;32m██║░░██║██████║██║░░░██║███████╗░░██║░░░██████║\033[1;33m║ 
\033[1;33m║\033[1;30m╚═╝░░╚═╝╚═════╝╚═╝░░░╚═╝╚══════╝░░╚═╝░░░╚═════╝\033[1;33m║ 
\033[1;33m║\033[1;30m░░░░╔██═╗░░╔███╗░░╔═██╗░░██═╗░░░██████═╗░░░░░░░\033[1;33m║ 
\033[1;33m║\033[1;31m░░░░╚╗██╚╗╔╝███╚╗╔╝██╔╝░████╚╗░░██░░░██╝░░░░░░░\033[1;33m║ 
\033[1;33m║\033[1;32m░░░░░╚╗██╚╝██░██╚╝██╔╝░██░░██╚╗░██████╚╗░░░░░░░\033[1;33m║ 
\033[1;33m║\033[1;33m░░░░░░╚╗████╔═╗████╔╝░████████╚╗██╔══██╚╗░░░░░░\033[1;33m║ 
\033[1;33m║\033[1;34m░░░░░░░╚╗██╔╝░╚╗██╔╝░██╔═════██║██║░░░██║░░░░░░\033[1;33m║ 
\033[1;33m║\033[1;35m░░░░░░░░╚══╝░░░╚══╝░░╚═╝░░░░░╚═╝╚═╝░░░╚═╝░░░░░░\033[1;33m║ 
\033[1;33m╠═══════════════════════════════════════════════╣
\033[1;33m║\033[1;34m▶ Nhóm Zalo  : \033[1;35mzalo.me/g/rbpywb976             \033[1;33m║
\033[1;33m║\033[1;34m▶ FaceBook : \033[1;35mfacebook.com/QuanHau210           \033[1;33m║
\033[1;33m║\033[1;34m▶ Zalo : \033[1;35m0961386638                            \033[1;33m║
\033[1;33m║\033[1;34m▶ Mua Key Vip Cứ Liên Hệ Zalo Nhé              \033[1;33m║
\033[1;33m║\033[1;34m▶ Nếu Có Lỗi Vui Lòng Báo Cho Facebook Nhé     \033[1;33m║
\033[1;33m╚═══════════════════════════════════════════════╝
\033[1;32m-------------------------------------------------"""

os.system('cls' if os.name == 'nt' else 'clear')
print(banner)

def reverse_string(s):
    return s[::-1]

def xePwjMDG(length):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))

def tLx6cpsx():
    url = 'https://api.mail.tm/domains'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['hydra:member']
        else:
            pass
            return None
    except Exception as e:
        print(f'{vua}{do}[×] Error: {e}')
        return None

def f9kSLNSXl():
    fake = Faker()
    mail_domains = tLx6cpsx()
    if mail_domains:
        domain = random.choice(mail_domains)['domain']
        username = xePwjMDG(10)
        password = fake.password()
        birthday = fake.date_of_birth(minimum_age=18, maximum_age=45)
        first_name = fake.first_name()
        last_name = fake.last_name()
        url = 'https://api.mail.tm/accounts'
        headers = {'Content-Type': 'application/json'}
        data = {'address': f'{username}@{domain}', 'password': password}
        try:
            response = requests.post(url, headers=headers, json=data)
            if response.status_code == 201:
                print(f'{vua}{xanh_la}[√] Email Created: {username}@{domain}')
                return (f'{username}@{domain}', password, first_name, last_name, birthday)
            else:
                pass
                return None, None, None, None, None
        except Exception as e:
            print(f'{vua}{do}[×] Error: {e}')
            return None, None, None, None, None
    return None, None, None, None, None

def get_cookie(email, password, token=None):
    """
    Hàm fix: Tránh garbled, retry, dùng token nếu có.
    """
    session = requests.Session()
    
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
            'Accept-Encoding': 'identity',  # Tránh garbled
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': 'no-cache',
            'Pragma': 'no-cache',
            'Referer': 'https://m.facebook.com/',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1'
        }
        session.headers.update(headers)
        session.cookies.clear()
        
        try:
            if token:
                print(f'{vua}{vang}[+] Dùng token từ registration...')
                session.headers['Authorization'] = f'Bearer {token}'
                home_resp = session.get('https://m.facebook.com/home.php', timeout=10)
                if 'c_user' in session.cookies:
                    cookies_dict = dict(session.cookies)
                    important_cookies = {k: v for k, v in cookies_dict.items() if k in ['c_user', 'xs', 'datr', 'fr', 'sb']}
                    cookie_str = '; '.join([f'{k}={v}' for k, v in important_cookies.items()])
                    print(f'{vua}{xanh_la}[√] Cookie từ token: {cookie_str}')
                    return cookie_str
                else:
                    print(f'{vua}{do}[×] Token không valid.')
            
            time.sleep(random.uniform(2, 5))
            print(f'{vua}{vang}[+] Warm up homepage (retry {retry+1}/{max_retries})...')
            home_url = 'https://m.facebook.com'
            home_resp = session.get(home_url, timeout=10)
            
            if len(home_resp.text) < 1000 or not home_resp.text.startswith('<!DOCTYPE'):
                print(f'{vua}{do}[×] Garbled tại home.')
                continue
            
            login_url = 'https://m.facebook.com/login.php'
            login_resp = session.get(login_url, timeout=10)
            
            if 'checkpoint' in login_resp.text.lower() or len(login_resp.text) < 1000:
                print(f'{vua}{do}[×] Checkpoint/garbled tại login.')
                continue
            
            lsd_match = re.search(r'name=["\']lsd["\'] value=["\']([^"\']+)["\']', login_resp.text)
            jazoest_match = re.search(r'name=["\']jazoest["\'] value=["\']([^"\']+)["\']', login_resp.text)
            lsd = lsd_match.group(1) if lsd_match else ''
            jazoest = jazoest_match.group(1) if jazoest_match else ''
            
            if not lsd or not jazoest:
                print(f'{vua}{do}[×] Không parse lsd/jazoest.')
                continue
            
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
                'bi_xrwh': '0'
            }
            
            time.sleep(random.uniform(1, 3))
            post_response = session.post(login_url, data=login_data, allow_redirects=True, timeout=10)
            
            post_text = post_response.content.decode('utf-8', errors='ignore') if len(post_response.text) < 500 else post_response.text
            
            if 'checkpoint' in post_text.lower():
                print(f'{vua}{do}[×] Checkpoint sau post: {email}')
                continue
            
            if post_response.status_code in [200, 302] and 'c_user' in session.cookies:
                print(f'{vua}{xanh_la}[√] Login OK cho: {email}')
                
                time.sleep(random.uniform(2, 4))
                homepage_resp = session.get('https://m.facebook.com/home.php', timeout=10)
                if 'checkpoint' in homepage_resp.text.lower():
                    print(f'{vua}{do}[×] Checkpoint sau warm up.')
                    continue
                
                fb_dtsg_match = re.search(r'name=["\']fb_dtsg["\'] value=["\']([^"\']+)["\']', homepage_resp.text)
                fb_dtsg = fb_dtsg_match.group(1) if fb_dtsg_match else ''
                print(f'{vua}{vang}[+] fb_dtsg: {fb_dtsg[:20]}...')
                
                cookies_dict = dict(session.cookies)
                important_cookies = {k: v for k, v in cookies_dict.items() if k in ['c_user', 'xs', 'datr', 'fr', 'sb', 'locale', 'm_pixel_ratio', 'act']}
                cookie_str = '; '.join([f'{k}={v}' for k, v in important_cookies.items()])
                
                print(f'{vua}{xanh_la}[+] Cookie: {cookie_str}')
                return cookie_str
            else:
                print(f'{vua}{do}[×] Post fail (status: {post_response.status_code}). Retry {retry+1}/{max_retries}')
                time.sleep(5)
        
        except Exception as e:
            print(f'{vua}{do}[×] Lỗi retry {retry+1}: {e}')
            continue  # Tiếp tục retry thay vì return ngay
    
    print(f'{vua}{do}[×] Tất cả retry fail cho {email}. Thử proxy hoặc login thủ công.')
    return None

def QuanHau(email, password, first_name, last_name, birthday):
    api_key = '882a8490361da98702bf97a021ddc14d'
    secret = '62f8ce9f74b12f84c123cc23437a4a32'
    gender = random.choice(['M', 'F'])

    req = {
        'api_key': api_key,
        'attempt_login': True,
        'birthday': birthday.strftime('%Y-%m-%d'),
        'client_country_code': 'EN',
        'fb_api_caller_class': 'com.facebook.registration.protocol.RegisterAccountMethod',
        'fb_api_req_friendly_name': 'registerAccount',
        'firstname': first_name,
        'format': 'json',
        'gender': gender,
        'lastname': last_name,
        'email': email,
        'locale': 'en_US',
        'method': 'user.register',
        'password': password,
        'reg_instance': xePwjMDG(32),
        'return_multiple_errors': True
    }

    sorted_req = sorted(req.items(), key=lambda x: x[0])
    sig = ''.join(f'{k}={v}' for k, v in sorted_req)
    ensig = hashlib.md5((sig + secret).encode()).hexdigest()
    req['sig'] = ensig

    api_url = 'https://b-api.facebook.com/method/user.register'
    response = requests.post(api_url, data=req)

    if response.status_code == 200:
        reg = response.json()
        id_ = reg.get('new_user_id')  # Đổi id thành id_ vì id là built-in
        token = reg.get('session_info', {}).get('access_token')
        print(
            f"""{vua}{xanh_la}[+] Email: {email}
{vua}{xanh_la}[+] Password: {password}
{vua}{xanh_la}[+] Name: {first_name} {last_name}
{vua}{xanh_la}[+] BirthDay: {birthday}
{vua}{xanh_la}[+] Gender: {gender}
==================================="""
        )
        print(f'{vua}{vang}[+] Đang lấy cookie...')
        cookie = get_cookie(email, password, token)
        if cookie:
            print(f'{vua}{xanh_la}[√] Cookie lưu cho: {email}')
            # Lưu file
            safe_email = email.replace('@', '_').replace('.', '_')
            with open(f'cookie_{safe_email}.txt', 'w') as f:
                f.write(cookie)
            print(f'{vua}{xanh_la}[+] Đã lưu file: cookie_{safe_email}.txt')
        else:
            print(f'{vua}{do}[×] Fail cookie: {email}')
    else:
        print(f'{vua}{do}[×] Registration Error: {response.text}')

def WcfriFTc(url, params, post=True):
    headers = {
        'User-Agent': '[FBAN/FB4A;FBAV/35.0.0.48.273;FBDM/{density=1.33125,width=800,height=1205};FBLC/en_US;FBCR/;FBPN/com.facebook.katana;FBDV/Nexus 7;FBSV/4.1.1;FBBK/0;]'
    }
    if post:
        response = requests.post(url, data=params, headers=headers)
    else:
        response = requests.get(url, params=params, headers=headers)
    return response.json()

def create_accounts(num_accounts):
    for i in range(num_accounts):
        email, password, first_name, last_name, birthday = f9kSLNSXl()
        if email and password and first_name and last_name and birthday:
            QuanHau(email, password, first_name, last_name, birthday)

# Main
try:
    num_accounts = int(input(f'{vua}[+] Muốn bao nhiêu tài khoản: {vang}'))
    create_accounts(num_accounts)
except ValueError:
    print(f'{vua}{do}[×] Input không hợp lệ. Dùng 1 acc.')
    create_accounts(1)
