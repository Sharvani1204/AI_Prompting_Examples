import openai
openai.api_key = "sk-or-v1-YOUR_REAL_KEY_HERE"
openai.api_base= "https://openrouter.ai/api/v1"
user_input= input("You: ")
reply= ""
response= openai.ChatCompletion.create(model= "nvidia/nemotron-nano-9b-v2:free", messages= [{"role": "system","content": "You are expert translator."},{"role":"user","content":"English: Good Moring\n French: Bonjour"}, {"role": "user", "content": f"English: {user_input}\nFrench: "}])
reply= response['choices'][0]['message']['content']
print(f"Chatbot: {reply}\n")