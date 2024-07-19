import chatglm_cpp

pipeline = chatglm_cpp.Pipeline("./models/chatglm-ggml.bin")
print(pipeline.chat([chatglm_cpp.ChatMessage(role="user", content="近年来，我国在军事科技领域取得了哪些重要突破？")]))
