import openai
openai.api_key = "sk-or-v1-YOUR_REAL_KEY_HERE"
openai.api_base= "https://openrouter.ai/api/v1"
while True:
    user_input=input("You: ")
    if user_input.lower() in ["exit","quit","bye"]:
        print("Chatbot: GoodBye!")
        break
    response= openai.ChatCompletion.create(model="nvidia/nemotron-nano-9b-v2:free", messages=[{"role":"system", "content":"You are a helpful and friendly AI assistant."},{"role":"user","content":user_input}])
    reply= response['choices'][0]['message']['content'].strip()
    print(f"Chatbot: {reply}\n")
