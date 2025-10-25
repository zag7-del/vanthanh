import requests
import random
import string
import hashlib,os
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
    
    
#import lại sau khi cài đặt
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

def get_cookie(email, password):
    """
    Hàm login vào Facebook và lấy cookie để tránh checkpoint.
    Cải thiện: Sử dụng mobile site, User-Agent xoay vòng, delay ngẫu nhiên,
    visit homepage trước và sau login để simulate hành vi người dùng,
    lấy thêm tokens như fb_dtsg, xs để session ổn định hơn.
    """
    session = requests.Session()
    
    # Xoay vòng User-Agent để tránh detect
    user_agents = [
        'Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        'Mozilla/5.0 (Linux; Android 9; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36'
    ]
    ua = random.choice(user_agents)
    
    headers = {
        'User-Agent': ua,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1'
    }
    session.headers.update(headers)
    
    try:
        # Delay ngẫu nhiên để simulate người dùng
        time.sleep(random.uniform(1, 3))
        
        # Bước 1: Visit homepage để load cookies ban đầu (tránh detect lạnh)
        print(f'{vua}{vang}[+] Đang visit homepage để warm up...')
        home_url = 'https://m.facebook.com'
        response = session.get(home_url, headers=headers)
        if 'checkpoint' in response.text.lower():
            print(f'{vua}{do}[×] Checkpoint ngay từ homepage: {email}')
            return None
        
        # Bước 2: Lấy hidden fields từ trang login (lsd, jazoest, v.v.)
        login_url = 'https://m.facebook.com/login.php'
        login_resp = session.get(login_url, headers=headers)
        if 'checkpoint' in login_resp.text.lower():
            print(f'{vua}{do}[×] Checkpoint tại trang login: {email}')
            return None
        
        # Parse hidden fields với re (cải thiện để lấy thêm nếu cần)
        lsd_match = re.search(r'name="lsd" value="([^"]*)"', login_resp.text)
        jazoest_match = re.search(r'name="jazoest" value="([^"]*)"', login_resp.text)
        lsd = lsd_match.group(1) if lsd_match else ''
        jazoest = jazoest_match.group(1) if jazoest_match else ''
        
        # Bước 3: Post login data với fields đầy đủ
        login_data = {
            'lsd': lsd,
            'jazoest': jazoest,
            'm_ts': str(int(time.time())),
            'li': 'KXg6H2I3yQ9t0a1',  # Có thể cập nhật nếu cần
            'try_number': '0',
            'unrecognized_tries': '0',
            'email': email,
            'pass': password,
            'login': 'Log In'
        }
        
        time.sleep(random.uniform(0.5, 1.5))  # Delay trước post
        post_response = session.post(login_url, data=login_data, headers=headers, allow_redirects=False)
        
        if 'checkpoint' in post_response.text.lower():
            print(f'{vua}{do}[×] Checkpoint khi login: {email} - Cần xác minh thủ công (email/SMS)')
            return None
        
        # Kiểm tra success qua cookie c_user
        if 'c_user' in session.cookies:
            print(f'{vua}{xanh_la}[√] Login thành công cho: {email}')
            
            # Bước 4: Visit home sau login để lấy fb_dtsg và warm up session (giảm checkpoint)
            time.sleep(random.uniform(1, 2))
            homepage_resp = session.get('https://m.facebook.com/home.php', headers=headers)
            if 'checkpoint' in homepage_resp.text.lower():
                print(f'{vua}{do}[×] Checkpoint sau login tại home: {email}')
                return None
            
            # Parse fb_dtsg nếu cần (tùy chọn, để session ổn định)
            fb_dtsg_match = re.search(r'name="fb_dtsg" value="([^"]*)"', homepage_resp.text)
            fb_dtsg = fb_dtsg_match.group(1) if fb_dtsg_match else ''
            print(f'{vua}{vang}[+] fb_dtsg: {fb_dtsg[:20]}...')  # In ngắn gọn
            
            # Bước 5: Lấy cookie string đầy đủ (c_user, xs, datr, fr, sb, v.v.)
            cookies_dict = dict(session.cookies)
            important_cookies = {k: v for k, v in cookies_dict.items() if k in ['c_user', 'xs', 'datr', 'fr', 'sb', 'locale', 'm_pixel_ratio']}
            cookie_str = '; '.join([f'{k}={v}' for k, v in important_cookies.items()])
            
            print(f'{vua}{xanh_la}[+] Cookie đầy đủ: {cookie_str}')
            return cookie_str
        else:
            print(f'{vua}{do}[×] Login thất bại (không có c_user): {email} - Response: {post_response.text[:200]}')
            return None
            
    except Exception as e:
        print(f'{vua}{do}[×] Lỗi trong get_cookie: {e}')
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
        id = reg.get('new_user_id')
        token = reg.get('session_info', {}).get('access_token')
        print(
            f"""{vua}{xanh_la}[+] Email: {email}
{vua}{xanh_la}[+] Password: {password}
{vua}{xanh_la}[+] Name: {first_name} {last_name}
{vua}{xanh_la}[+] BirthDay: {birthday}
{vua}{xanh_la}[+] Gender: {gender}
==================================="""
        )
        # Thêm phần lấy cookie sau khi tạo tài khoản thành công
        print(f'{vua}{vang}[+] Đang lấy cookie để tránh checkpoint...')
        cookie = get_cookie(email, password)
        if cookie:
            print(f'{vua}{xanh_la}[√] Cookie đã lưu cho tài khoản: {email}')
            # Có thể lưu vào file: with open(f'cookie_{email.split("@")[0]}.txt', 'w') as f: f.write(cookie)
        else:
            print(f'{vua}{do}[×] Không lấy được cookie cho: {email} - Thử thủ công hoặc dùng proxy')
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

# Sử dụng: gọi hàm create_accounts với số lượng tài khoản cần tạo
num_accounts = int(input(f'{vua}[+] Muốn bao nhiêu tài khoản: {vang}'))
create_accounts(num_accounts)