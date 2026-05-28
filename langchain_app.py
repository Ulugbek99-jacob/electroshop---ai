from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

model = OllamaLLM(model="llama3.2")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{question}")
])

chain = prompt | model
history = []

print("Chatbot (exit - chiqish)")
print("-" * 40)

while True:
    user_input = input("Siz: ")
    if user_input.lower() == "exit":
        break
    
    response = chain.invoke({
        "history": history,
        "question": user_input
    })
    
    history.append(HumanMessage(content=user_input))
    history.append(AIMessage(content=response))
    
    print(f"AI: {response}")
    print("-" * 40)