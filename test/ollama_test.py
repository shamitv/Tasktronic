from dotenv import load_dotenv
from langchain_ollama import ChatOllama

load_dotenv()

llm = ChatOllama(
    model = "qwen2.5:14b"
)

messages = [
    ("system", "You are a helpful translator. Translate the user sentence to Hindi."),
    ("human", "I love programming."),
]

llm.invoke(messages)