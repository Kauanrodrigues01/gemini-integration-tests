"""
Explicação sobre o Modo de Streaming:

No modo de streaming do Gemini, as respostas são geradas e enviadas em partes incrementais, ou "chunks", em vez de uma única resposta completa de uma vez. Isso é útil principalmente em situações interativas, como chats em tempo real, onde o objetivo é exibir o conteúdo conforme ele é gerado, sem precisar esperar que toda a resposta seja completada.

O streaming permite que o modelo envie o texto enquanto ainda está processando, o que resulta em uma experiência mais dinâmica e imediata para o usuário. Cada "chunk" é uma parte da resposta gerada, que pode ser usada conforme é recebida. Isso melhora a performance em aplicações que precisam de respostas rápidas e contínuas, como em sistemas de bate-papo (chatbots).
"""


from google import generativeai as genai
from decouple import config

API_KEY = config('API_KEY', cast=str)

genai.configure(api_key=API_KEY)

generation_config = {
    "temperature": 2,  # Controla a aleatoriedade das respostas
    "top_p": 1,        # Nível de diversidade das respostas
}

system_instruction = "Você é um assistente amigável e técnico que responde de forma concisa."

model = genai.GenerativeModel('gemini-1.5-flash', generation_config=generation_config, system_instruction=system_instruction)

def generate_with_stream(prompt):
    response = model.generate_content(
        contents=[prompt],
        stream=True  # Ativa o modo de streaming
    )

    # Itera sobre as partes da resposta conforme são geradas
    for chunk in response:
        print(chunk.text)  # Processa o texto da resposta
        # Aqui você pode adicionar lógica adicional, como exibir no front-end ou salvar

# Testando a função
generate_with_stream("Fale sobre django")