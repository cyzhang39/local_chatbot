import streamlit as st
import time
from apps.utils import load_pdf, text_split, save_embeddings, get_embeddings
from langchain.chains import RetrievalQA
from langchain_community.llms import ChatGLM
import os



# Initialize the LLM

MODEL = os.getenv('MODEL_URL', 'http://localhost:8000')
llm = ChatGLM(endpoint_url=MODEL, temperature=0.01, stream=True)

# @st.cache_data(persist=True)
def load_and_process_documents():
    docs = load_pdf()
    chunks = text_split(docs)
    start = time.time()
    db = save_embeddings(chunks)
    end = time.time()
    return db, end - start

def load_saved_documents():
    start = time.time()
    db = get_embeddings()
    end = time.time()
    return db, end - start

# Define the main function for the Streamlit app
def main():
    st.title("AI客服测试")
    
    # Define the directory containing the PDF files
    # directory = "./docs"
    
    # Load and process documents
    st.write("加载处理知识文档中。。。")
    if 'docs' not in st.session_state:
        st.session_state['docs'] = 1
        db, encoding_time = load_and_process_documents()
        st.write(f"处理完成，用时：{encoding_time:.2f}s")
    else:
        db, encoding_time = load_saved_documents()
    retriever = db.as_retriever()
    
    # Initialize the QA chain
    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)
    
    # Chat interface
    if 'history' not in st.session_state:
        st.session_state['history'] = []
    
    query = st.text_input("输入问题")
    
    if st.button("确认"):
        if query:
            st.session_state['history'].append({"query": query})
            
            # Generate answer
            st.write("clear-3分钟）")
            start = time.time()
            response = qa.invoke(query)
            end = time.time()
            st.session_state['history'][-1]["response"] = response['result']
            st.write(f"生成回答用时: {end - start:.2f}s")
    
    # Display chat history
    for chat in st.session_state['history']:
        st.write(f"**问题:** {chat['query']}")
        st.write(f"**回答:** {chat['response']}")

if __name__ == '__main__':
    main()
