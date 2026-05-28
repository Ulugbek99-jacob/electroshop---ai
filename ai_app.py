import ollama

messages = []

print("AI Chatbot (chiqish uchun 'exit' yozing)")
print("-" * 40)

while True:
    user_input = input("Siz: ")
    
    if user_input.lower() == "exit":
        print("Xayr!")
        break
    
    messages.append({"role": "user", "content": user_input})
    
    response = ollama.chat(
        model="llama3.2",
        messages=messages
    )
    
    ai_message = response.message.content
    messages.append({"role": "assistant", "content": ai_message})
    
    print(f"AI: {ai_message}")
    print("-" * 40)