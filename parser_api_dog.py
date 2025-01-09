import requests
# from urllib3 import request
from  random import randint


def get_image_link(url: str) -> str:
    response = requests.get(url)
    data = response.json()
    link = data.get("message")

    return link

def download_image(url: str) -> None:
    response = requests.get(url)
    image = response.content
    with open("image.jpg", "wb") as f:
        f.write(image)

api_url = "https://dog.ceo/api/breeds/image/random"
link = get_image_link(url=api_url)
print(link)
download_image(url=link)

print(randint(1,1000))

