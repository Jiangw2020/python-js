import base64
import hashlib

base64_data = base64.b64encode('Fnqzuji2fIft8bhgFKAq'.encode())
replace_data = base64_data.replace(b'=', b'')
result = hashlib.md5(replace_data).hexdigest()

print(result)