
import os
import requests
from urllib.parse import quote


# export GITLAB_TOKEN="your_actual_gitlab_token"

# GitLab project configuration
PROJECT_ID = 83984781
BASE_URL = (
    f"https://gitlab.com/api/v4/projects/"
    f"{PROJECT_ID}/repository/branches"
)

GITLAB_TOKEN = os.getenv("GITLAB_TOKEN")

# Keep True until you verify the branch list
DRY_RUN = True

if not GITLAB_TOKEN:
    raise SystemExit("GitLab token is missing")

headers = {"PRIVATE-TOKEN": GITLAB_TOKEN}


def urlcheck():
    branches = []
    page = 1

    try:
        while True:
            response = requests.get(
                BASE_URL,
                headers=headers,
                params={"per_page": 100, "page": page},
                timeout=10
            )

            response.raise_for_status()
            page_data = response.json()

            if not page_data:
                break

            for branch in page_data:
                branches.append(branch["name"])

            if len(page_data) < 100:
                break

            page += 1

        return branches

    except requests.exceptions.RequestException as e:
        print("Failed to fetch branches:", e)
        return None


def branch_featurefetch():
    branch_names = urlcheck()

    if branch_names is None:
        return None

    return [
        name for name in branch_names
        if name.startswith("feature")
    ]


def branch_delete_feature():
    feature_branches = branch_featurefetch()

    if feature_branches is None:
        print("Stopping: unable to fetch branches.")
        return

    if not feature_branches:
        print("No matching feature branches found.")
        return

    print("Matching branches:", feature_branches)

    if DRY_RUN:
        for branch in feature_branches:
            print("DRY RUN - Would delete:", branch)
        return

    confirmation = input(
        "Type DELETE to confirm deleting these branches: "
    )

    if confirmation != "DELETE":
        print("Deletion cancelled.")
        return

    for branch in feature_branches:
        try:
            encoded_branch = quote(branch, safe="")
            delete_url = f"{BASE_URL}/{encoded_branch}"

            response = requests.delete(
                delete_url,
                headers=headers,
                timeout=10
            )

            if response.status_code == 204:
                print("Deleted successfully:", branch)
            else:
                print(
                    "Failed:", branch,
                    "Status:", response.status_code,
                    "Response:", response.text
                )

        except requests.exceptions.RequestException as e:
            print("Request error for", branch, ":", e)


branch_delete_feature()
