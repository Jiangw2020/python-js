import base64
import hashlib
import os
from io import BytesIO

import urllib3
from urllib3.exceptions import InsecureRequestWarning
# 禁用SSL警告
urllib3.disable_warnings(InsecureRequestWarning)
import subprocess
from functools import partial

# subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
# with open('猿人学web-07.js', 'r+', encoding='utf-8') as f:
#     js_code = f.read()
#
# import execjs
# ctx = execjs.compile(js_code)
base64_data = base64.b64encode('Fnqzuji2fIft8bhgFKAq'.encode())
replace_data = base64_data.replace(b'=', b'')
result = hashlib.md5(replace_data).hexdigest()

file_name = '0.txt'
file_dir = os.getcwd() + '/07/'

woff = 'AAEAAAAKAIAAAwAgT1MvMv3SNqIAAAEoAAAAYGNtYXCOTG1GAAABpAAAAYpnbHlma7aE0AAAA0gAAAP8aGVhZCBtNWkAAACsAAAANmhoZWEG1gEtAAAA5AAAACRobXR4ArwAAAAAAYgAAAAabG9jYQU4BlgAAAMwAAAAGG1heHABGABFAAABCAAAACBuYW1lUGhGMAAAB0QAAAJzcG9zdCPfY1oAAAm4AAAAiAABAAAAAQAAbMBmVF8PPPUACQPoAAAAANnIUd8AAAAA5P'
