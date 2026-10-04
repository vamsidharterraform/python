# # project id: 83984781

import requests

GITLAB_TOKEN='glpat-KR0RAdUhjOV-MkClYWOMUGM6MQpvOjEKdTpwbTRidg8.01.170p2ug5u'

url = "https://gitlab.com/api/v4/projects/83984781/repository/branches"
# url='https://invalid-hostname-12345.example'

headers = {
    "PRIVATE-TOKEN": GITLAB_TOKEN
}
branches=[]
if not GITLAB_TOKEN:
    print("GitLab token is missing or empty")
else:
    print("GitLab token is available")

def urlcheck():
    try:
        response = requests.get(url, headers=headers, timeout=10)

        print("Status code:", response.status_code)

        if response.status_code == 200:
            for branch in response.json():
                branches.append(branch["name"])
            return branches
        else:
            print("Request failed:", response.text)
            return []

    except requests.exceptions.Timeout:
        print("Request timed out")
        return []

    except requests.exceptions.ConnectionError:
        print("Connection failed. Check your network or GitLab connectivity")
        return []  
    except requests.exceptions.RequestException as e:
        print("Request error:", e)
        return []

feature_branches = []

def branch_featurefetch():
    branch_names = urlcheck()
    # print("branches are :", branch_names)
    for branch in branch_names:
        if branch.startswith("feature"):
            feature_branches.append(branch)
    return feature_branches
    # print("feature branch:" , feature_branches)





def branch_delete_feature():
    feature_branches = branch_featurefetch()
    print (feature_branches)
    for feat in feature_branches:
        try:
            delete_url = f"{url}/{feat}"
            response = requests.delete(
                delete_url,
                headers=headers,
                timeout=10
            )
            if response.status_code == 204:
                print("Branches deleted successfully:", feat)
            else:
                print(response.status_code)
                print("Failed to delete the branches")
        except requests.exceptions.RequestException as e:  # Change 3
            print("Request error:", e)

branch_delete_feature()