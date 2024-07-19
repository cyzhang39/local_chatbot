from langchain_community.llms import ChatGLM
# from core.config import settings


llm = ChatGLM(endpoint_url="http://127.0.0.1:8000")
answer = llm.invoke("你好")
print(answer)

'你好👋！我是人工智能助手 ChatGLM2-6B，很高兴见到你，欢迎问我任何问题。'