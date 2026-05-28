import requests

response = requests.get("https://jsonplaceholder.typicode.com/users/1")

if response.status_code == 200:
    user = response.json()
    print(f"Ism: {user['name']}")
    print(f"Email: {user['email']}")
    print(f"Shahar: {user['address']['city']}")
else:
    print("Xato!")