from apps.utils import load_pdf, text_split, save_embeddings, get_embeddings

from langchain.chains import RetrievalQA
from langchain_community.llms import ChatGLM



import time

def main():
    llm = ChatGLM(endpoint_url="http://127.0.0.1:8000", temperature=0.01, stream=True)
    
    # 文档加载和分片
    docs = load_pdf()
    chunks = text_split(docs)
    
    # 编码
    start = time.time()
    db = save_embeddings(chunks)
    end = time.time()
    print(f"编码用时：{end-start}s")
    
    retriever = db.as_retriever()
    
    # 问答链
    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)
    
    query = "请介绍一下MPI TS3000系列"

    # 生成回答
    start = time.time()
    response = qa.invoke(query)
    end = time.time()
    print(f"生成用时：{end-start}s")
    
    print(response)

if __name__ == '__main__':
    main()
