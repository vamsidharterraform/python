import requests

GITLAB_TOKEN='glpat-KR0RAdUhjOV-MkClYWOMUGM6MQpvOjEKdTpwbTRidg8.01.170p2ug5u'

url = "https://gitlab.com/api/v4/projects/83984781/repository/branches"
# url='https://invalid-hostname-12345.example'

headers = {
    "PRIVATE-TOKEN": GITLAB_TOKEN
}


if not headers:
    print("hearders is empty")

branch = []
def urlcheck():
    response = requests.get(url, headers=headers, timeout=10)
    try:
        if response.status_code == 200:
            for branch in response.json():
                branch = branch["name"]
                print(branch)
            print("url reached successfully")
        else:
            print("url is not reacheable")

    except requests.exceptions.RequestException() as e:
        print("issue in requesting the url" , e)

urlcheck()

