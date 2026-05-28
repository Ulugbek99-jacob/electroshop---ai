from pypdf import PdfReader
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# PDF o'qish
reader = PdfReader("/Users/ulugbek/Desktop/python-lessons/Eshboltaev_Ulugbek_Resume.pdf")
text = ""
for page in reader.pages:
    text += page.extract_text()

print("PDF o'qildi!")
print(f"Sahifalar soni: {len(reader.pages)}")

# AI ga savol berish
model = OllamaLLM(model="llama3.2")

prompt = ChatPromptTemplate.from_messages([
    ("system", f"You are a helpful assistant. Use this document to answer questions:\n\n{text}"),
    ("human", "{question}")
])

chain = prompt | model

# Savol berish
while True:
    user_input = input("Savol: ")
    if user_input.lower() == "exit":
        break
    response = chain.invoke({"question": user_input})
    print(f"AI: {response}\n")