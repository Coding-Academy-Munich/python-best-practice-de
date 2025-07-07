import requests
from PIL import Image
from PIL.ImageShow import show

response = requests.get("https://www.python.org/static/img/python-logo.png")
with open("python-logo.png", "wb") as file:
    file.write(response.content)
image = Image.open("python-logo.png")
show(image)
