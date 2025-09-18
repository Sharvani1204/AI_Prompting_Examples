import openai
openai.api_key = "sk-or-v1-YOUR_REAL_KEY_HERE"
openai.api_base= "https://openrouter.ai/api/v1"
user_input= input("You: ")
reply= ""
response= openai.ChatCompletion.create(model= "nvidia/nemotron-nano-9b-v2:free", messages= [{"role": "system","content": "You are helpful assistant."},{"role":"user","content":f"{user_input}\n Think step by step."}, {"role": "assistant", "content": reply}])
reply= response['choices'][0]['message']['content']
print(f"Chatbot: {reply}\n")