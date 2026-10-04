import requests

GITLAB_TOKEN='glpat-KR0RAdUhjOV-MkClYWOMUGM6MQpvOjEKdTpwbTRidg8.01.170p2ug5u'

project_id = 83984781
url = f"https://gitlab.com/api/v4/projects/{project_id}/repository/branches"

headers = {
    "PRIVATE-TOKEN": GITLAB_TOKEN
}

branch_names = ["feature1", "feature2", "feature3"]


def create_branches():
    for branch_name in branch_names:
        try:
            response = requests.post(
                url,
                headers=headers,
                data={
                    "branch": branch_name,
                    "ref": "main"
                },
                timeout=10
            )

            if response.status_code == 201:
                print("Branch created successfully:", branch_name)

            else:
                print("Unable to create branch:", branch_name)
                print("Status code:", response.status_code)
                print("Response:", response.text)

        except requests.exceptions.RequestException as e:
            print("Request failed for", branch_name, ":", e)


create_branches()