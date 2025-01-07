from google import generativeai as genai
from decouple import config

API_KEY = config('API_KEY', cast=str)

genai.configure(api_key=API_KEY)

generation_config = genai.GenerationConfig(
    max_output_tokens=100,
    temperature=0.7,
    top_p=1
)

system_instruction = "Você é um assistente amigável e técnico que responde de forma concisa."

model = genai.GenerativeModel('gemini-1.5-flash', generation_config=generation_config, system_instruction=system_instruction)

response = model.generate_content("Me fale curiosidades sobre a IA do google")

print(response.text)