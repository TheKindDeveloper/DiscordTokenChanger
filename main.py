import requests
import string
import secrets
from Dickscord import Style
from pystyle import *
import os
import random

def _CHECKER_():
    os.system('title Bypass Token Changer ')
    custompass = Style.input("(#): Custom password [y/n]?: ")
    if custompass == "y":
        newpassx = Style.input("(#): New Password?: ")

    def generate_password(length=12):
        alphabet = string.ascii_letters + string.digits
        while True:
            password = ''.join(secrets.choice(alphabet) for i in range(length))
            if ':' not in password and '@' not in password:
                break
        return password

    def export_tokens():
        with open('tokens.txt', 'r') as f:
            tokens = f.readlines()
        tokens = [x.strip() for x in tokens]
        return tokens

    combo = export_tokens()

    class Dickcord_extension:
        def __init__(self):
            self.cookie = None
            self.fingerprint = None

        def get_cookies(self):
            response = requests.get("https://discord.com")
            self.cookie = response.cookies.get_dict()
            self.cookie['locale'] = "us"

        def request_fingerprint(self, headers):
            response = requests.get("https://discordapp.com/api/v9/experiments", headers=headers)
            self.fingerprint = response.json()["fingerprint"]

        def generate_user_agent(self):
            user_agents = [
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0"
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58",
            ]
            return random.choice(user_agents)

        def cookies(self):
            if self.cookie is None:
                Style.print("(!): Couldn't Fetch Cookies.")
            return self.cookie

        def get_fingerprint(self):
            if self.fingerprint is None:
                Style.print("(!): Couldn't Fetch Fingerprints.")
            return self.fingerprint

        def cookieshead(self):
            cookies_dict = self.cookies()
            return "; ".join([f"{key}={value}" for key, value in cookies_dict.items()])

        def generate_xsuperproperty(self):
            properties = [
                "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImRlIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExMi4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMTIuMC4xNzIyLjU4IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTEyLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE5MzkwNiwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ==",
                "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImRlIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExNS4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMTUuMC4xOTAxLjIwMyIsImJyb3dzZXJfdmVyc2lvbiI6IjExNS4wLjAuMCIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiIiwicmVmZXJyaW5nX2RvbWFpbiI6IiIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoyMjA0MDQsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
            ]
            return random.choice(properties)

    def change_password(email, password, token):
        Dickcord_extension().request_fingerprint(headers)
        fingerprint = Dickcord_extension().get_fingerprint()     
        user_agent = Dickcord_extension().generate_user_agent()   
        s = requests.Session()
        Dickcord_extension().get_cookies()
        cookies_header = Dickcord_extension().cookieshead()
        xsupaprop = Dickcord_extension().generate_xsuperproperty()

        headers = {'authorization': token,
                   'user-agent': user_agent,
                   'origin': 'discord.com',
                   'accept': '*/*',
                   'accept-encoding': 'gzip, deflate, br',
                   'cookie': cookies_header,
                   'sec-ch-ua': '"Chromium";v="112", "Microsoft Edge";v="112", "Not:A-Brand";v="99"',
                   'x-discord-locale': 'de',
                   'sec-ch-ua-platform': 'Windows',
                   'x-debug-options': 'bugReporterEnabled',
                   'sec-fetch-mode': 'cors',
                   'sec-fetch-site': 'same-origin',
                   'sec-ch-ua-mobile': '?0',
                   'x-super-properties': xsupaprop,
                   'x-fingerprint': fingerprint}

        s.get('https://discord.com/channels/@me', headers=headers)
        if custompass == "n":
            new = generate_password()
        else:
            new = newpassx

        payload = {
            'password': password,
            'new_password': new,
        }
        r = s.patch('https://discord.com/api/v9/users/@me', headers=headers, json=payload)
        new_token = r.json()['token']
        if r.status_code == 200:
            Style.print(f"(+): Changed ({email}) → {new_token}")
            return f'1:{email}:{new}:{new_token}'
        if r.status_code == 403:
            Style.print(f"(!): Couldn't Change {email} → {token} is locked")
        else:
            Style.print(f"(!): Failed to change for → ({email})")
            return f'0:{email}:{password}:{token}'

    def main_thread():
        for i in combo:
            email = i.split(':')[0]
            password = i.split(':')[1]
            token = i.split(':')[2]
            new_combo = change_password(email, password, token)
            if new_combo.split(':')[0] == '1':
                with open('new_tokens.txt', 'a') as f:
                    f.write(new_combo.split(':')[1] + ':' + new_combo.split(':')[2] + ':' + new_combo.split(':')[3] + '\n')
            else:
                with open('failed.txt.txt', 'a') as f:
                    f.write(new_combo.split(':')[1] + ':' + new_combo.split(':')[2] + ':' + new_combo.split(':')[3] + '\n')

    dsn = '''
     ▄▄▄▄ ▓██   ██▓ ██▓███   ▄▄▄        ██████   ██████ 
    ▓█████▄▒██  ██▒▓██░  ██▒▒████▄    ▒██    ▒ ▒██    ▒ 
    ▒██▒ ▄██▒██ ██░▓██░ ██▓▒▒██  ▀█▄  ░ ▓██▄   ░ ▓██▄   
    ▒██░█▀  ░ ▐██▓░▒██▄█▓▒ ▒░██▄▄▄▄██   ▒   ██▒  ▒   ██▒
    ░▓█  ▀█▓░ ██▒▓░▒██▒ ░  ░ ▓█   ▓██▒▒██████▒▒▒██████▒▒
    ░▒▓███▀▒ ██▒▒▒ ▒▓▒░ ░  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░
    ▒░▒   ░▓██ ░▒░ ░▒ ░       ▒   ▒▒ ░░ ░▒  ░ ░░ ░▒  ░ ░
     ░    ░▒ ▒ ░░  ░░         ░   ▒   ░  ░  ░  ░  ░  ░  
     ░     ░ ░                    ░  ░      ░        ░  
          ░░ ░ '''
    print(Colorate.Horizontal(Colors.blue_to_cyan, Center.XCenter(dsn)))
    Style.print("(#): Press Enter to start.")
    input("")
    main_thread()

_CHECKER_()
Style.input("\n(#): Done Changing all Tokens.")
