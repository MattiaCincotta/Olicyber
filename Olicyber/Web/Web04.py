import requests

url = "http://web-04.challs.olicyber.it/users"
headers = {
    "Accept": "application/xml"
}

response = requests.get(url, headers=headers)
print(response.text)
