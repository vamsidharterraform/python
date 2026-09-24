import requests
import sys
urls = [
    "https://jsonplaceholder.typicode.com/users",
    "https://wrong-url-example123.com",
    "https://jsonplaceholder.typicode.com/posts"
]


for url in urls:

    try:
        response = requests.get(url , timeout=5)
        if response.status_code == 200:
            print(url , "is accessible")
        else:
            print(url , "is nor accessible")
    
    except requests.exceptions.RequestException as e:
        print("failed , api requestfailed")