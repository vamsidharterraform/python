import requests

tokn="cccsvdv"
url="cscdcdvdv"

headers = {

    "PRIVATE-TOKEN" : tokn
}


def checkurl():
    response = requests.get(url, headers=headers, timeout=10)

    if requests.status_codes == 200:
        branches = reponse.json