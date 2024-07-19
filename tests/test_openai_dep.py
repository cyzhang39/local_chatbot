from openai import OpenAI
 
# client = OpenAI(base_url="http://127.0.0.1:8000/v1", api_key="123")
client = OpenAI(
        api_key="API",
        base_url="http://129.211.188.75:9090/v1"
)
messges = []

response = client.chat.completions.create(
    model="glm-4", 
    messages=[{"role": "user", "content": "介绍一下导弹"}],
    temperature=0.01,
    top_p=0.4,
    stream=False
)

print(response.choices[0].message.content)




print(response.choices[0].message.content)

'你好👋！我是人工智能助手 ChatGLM3-6B，很高兴见到你，欢迎问我任何问题。'