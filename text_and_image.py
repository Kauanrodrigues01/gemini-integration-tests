from google import generativeai as genai
from decouple import config
from PIL import Image

API_KEY = config('API_KEY', cast=str)

genai.configure(api_key=API_KEY)


model = genai.GenerativeModel("gemini-1.5-flash")
dog_image = Image.open("./images/dog_image.jpg")
response = model.generate_content(["Me fale sobre essa imagem, o que tem nela?", dog_image], stream=True)


for chuck in response:
    print(chuck.text, end="")