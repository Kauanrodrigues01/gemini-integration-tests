from google import generativeai as genai
from decouple import config
from PIL import Image

API_KEY = config('API_KEY', cast=str)

genai.configure(api_key=API_KEY)

generation_config = genai.GenerationConfig(
    max_output_tokens=200
)

system_instruction="Você é um assistente virtual de uma empresa 'TecnologiaTech'.A TecnologiaTech é uma empresa especializada no desenvolvimento de aplicativos móveis e aplicações web. Para o desenvolvimento de aplicativos móveis, a empresa utiliza tecnologias como Kotlin, React Native e Flutter, enquanto para aplicações web, emprega Python, Django, Django Rest Framework (DRF), React e Next.js. Trabalhamos com banco de dados relacionais(MySQL e PostgreSQL) e não relacionais(MongoDB). Sempre limite sua resposta até 200 tokens, quando re refiro a tokens, falo sobre a 'unidade de medida das palavras' que as IAs tem."

model = genai.GenerativeModel(
    'gemini-1.5-flash', 
    system_instruction=system_instruction, 
    generation_config=generation_config
)

dog_image = Image.open("./images/dog_image.jpg")

chat = model.start_chat(
    history=[
        {"role": "user", "parts": ["Olá, meu nome é kauan, tenho 16 anos e sou programador. Vou lhe enviar uma foto do meu cachorro", dog_image]},
        {"role": "model", "parts": "Olá, sou a IA do google"}
    ]
)

response = chat.send_message("Qual meu nome?", stream=True)
for chunk in response:
    print(chunk.text, end="")
    

print()

response = chat.send_message("Quantos anos eu tenho?", stream=True)
for chunk in response:
    print(chunk.text, end="")
    
print()    

response = chat.send_message("Me fale o que é preciso para trabalhar como desenvolvedor Web na empresa de vocês", stream=True)
for chuck in response:
    print(chuck.text, end="")
    
    
print()


response = chat.send_message("Qual a raça do meu cachorro?", stream=True)
for chuck in response:
    print(chuck.text, end="")
