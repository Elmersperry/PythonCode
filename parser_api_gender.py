import requests

# url = "https://api.genderize.io?name=misha"
# print(requests.get(url).json())

def get_gender_data(name: str) -> dict:
    params = {
        "name": name
    }
    url = "https://api.genderise.io/"
    response = requests.get(url, params=params)
    data = response.json()
    return data

def parse_gender_data(data: dict) -> None:
    pass

gender_data = get_gender_data(name="Alena")
print(gender_data)
print(parse_gender_data(data=gender_data))
