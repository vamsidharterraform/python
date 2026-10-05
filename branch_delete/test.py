import requests

GITLAB_TOKEN='glpat-KR0RAdUhjOV-MkClYWOMUGM6MQpvOjEKdTpwbTRidg8.01.170p2ug5u'

url = "https://gitlab.com/api/v4/projects/83984781/repository/branches"

headers = {
    'PRIVATE-TOKEN': GITLAB_TOKEN
}

if not GITLAB_TOKEN:
    print("empty")
else:
    print("valid value")

branch_list = []

def urlcheck():

    try:
        response = requests.get(url , headers=headers, timeout=10)
        if response.status_code == 200:
            for branch in response.json():
                branch_list.append(branch["name"])
            return branch_list
        else:
            print("Filed to fetch the url :", response.text)

    except requests.ConnectionError as e:
        print("connection error is :" , e)


feature_branches = []
def filterfeatbranch():
    branches = urlcheck()
    for feat in branches:
        if feat.startswith("feat"):
            feature_branches.append(feat)
    return feature_branches





def delete():
    fts = filterfeatbranch()
    for feats in fts:
        delete_url = f"{url}/{feats}"
        try:
            response = requests.delete(delete_url, headers=headers, timeout=10)
            if response.status_code == 204:
                print("deleted the branch successfully : ", feats)
            else:
                print("delete failed for the branch:" , feats)


        except requests.ConnectionError as e:
            print("delete failed")       

delete() 

