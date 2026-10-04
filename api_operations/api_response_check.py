import requests
import sys
urls = [
    "https://jsonplaceholder.typicode.com/users",
    "https://wrong-url-example123.com",
    "https://jsonplaceholder.typicode.com/posts"
]


for url in urls:
    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            print(url, "is accessible")
        else:
            print(url, f"is not accessible - HTTP {response.status_code}")

    except requests.exceptions.Timeout:
        print(url, "request timed out")

    except requests.exceptions.ConnectionError:
        print(url, "connection failed")

    except requests.exceptions.RequestException as e:
        print(url, "request failed:", e)