from requests.api import patch
from qinglong import qinglong
from json import loads,dumps
from re import findall
from requests import get
from urllib.parse import urlencode
from time import sleep
from os.path import dirname,abspath




CODES = {
    'city': ['MyCity',2]
}




PATH = dirname(abspath(__file__))

with open(PATH+'/config.py','r',encoding='utf-8') as r:
    config = loads(r.read())

username = config['username']
password = config['password']
host = config['host']
codes = CODES or config['codes']
default_user = config.get('default_user', range(1, 6))
bot_token = config['bot_token']
chat_id = config['chat_id']

ql = qinglong(host=host, username=username, password=password)
ql.login()
result = ql._get_logs_list().json()
 
for r in result['dirs']:
    if r['name'] == 'code':
        print(max(r['files']))
        file = max(r['files'])
        result = ql.get_log_file('code', file)
        with open(f'/root/item/jd_beans/{file}', 'w', encoding='utf-8') as w:
            w.write(result.json()['data'])
        log = result.json()['data']
  
for code_bot, code_log in codes.items():
    _codes = []
    number = 5
    if isinstance(code_log,list) and len(code_log)==2:
        code_log, number = code_log
    user = []
    for i in default_user:
        
        code = findall(f"{code_log}{i}=(.*)",log)
        print('code:', code, f"{code_log}{i}=(.*)",log)
        #code = findall(f"{code_log}{i}='(.*?)'",log)
        if len(code) != 1: continue
        code = code[0]
        if code:
            user.append(i)
            _codes.append(code)
    if len(_codes) < number:
        i = max(user)+1
        while 1:
            
            if i > ql.users or len(user) == number:
                break
            code = findall(f"{code_log}{i}=(.*)", log)
            print('code:', code, f"{code_log}{i}=(.*)", log)
            i += 1
            if len(code) != 1:
                continue
            code = code[0]
            if code:
                _codes.append(code)

    code = '&'.join(_codes)
    text = f'/submit_activity_codes {code_bot} {code}'
    query_params = {
        'chat_id':chat_id,
        'text': f'forward_message_to:#TuringLabbot#{text}'
    }
    
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage?{urlencode(query_params)}'
    result = get(url)
    #sleep(1)
    print(result.text)
