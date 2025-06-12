import os
import streamlit as st
import pickle
import time
import langchain
from langchain_cohere import ChatCohere
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.chains.qa_with_sources.loading import load_qa_with_sources_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain_community.embeddings import CohereEmbeddings
from langchain.vectorstores import FAISS
from dotenv import dotenv_values

env_vars = dotenv_values('/home/zero/VSC/AiML/GenAI/.env')
cohere_api = env_vars.get("CohereAPIKey")

st.title("Article Research Tool")
st.sidebar.title("Provide Article URLs")

urls=[]
for i in range(3):
    url = st.sidebar.text_input(f"URL {i+1}")
    urls.append(url)


process_url_clicked = st.sidebar.button("Process URLs")

st.sidebar.write("")
st.sidebar.write("")

st.sidebar.markdown(
    "### Usage:\n"
    "- Enter the URLs  \n"
    "- Click on 'Process URLs' Button  \n"
    "- Wait till it loads  \n"
    "- Ask your Questions"
)

main_placeholder = st.empty()
if process_url_clicked:
    #load data
    loader = UnstructuredURLLoader(urls=urls)
    data = loader.load()

    #split data
    splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n","\n",".",","],
        chunk_size=1000,
        chunk_overlap=200
    )
    main_placeholder.text("Text Splitter Started...")
    docs= splitter.split_documents(data)

    #create Embeddings
    embeddings = CohereEmbeddings(
        cohere_api_key=cohere_api,
        model="embed-english-v3.0", 
        user_agent="langchain"
    )
    # Create FAISS vector index
    vectorindex_cohere = FAISS.from_documents(docs, embeddings)
    main_placeholder.text("Embedding vector started Building...")
    time.sleep(2)

    main_placeholder.text("Saving vector DB...")
    try:
        vectorindex_cohere.save_local("faiss_cohere_index")
        main_placeholder.text("Vector DB saved successfully!")
    except Exception as e:
        main_placeholder.text(f"Error saving vector DB: {str(e)}")


query = main_placeholder.text_input("Question: ")

if query:
    if os.path.exists("faiss_cohere_index"):
        try:
            # Recreate embeddings for loading
            embeddings = CohereEmbeddings(
                cohere_api_key=cohere_api,
                model="embed-english-v3.0",
                user_agent="langchain"
            )
            vectorIndex = FAISS.load_local(
                "faiss_cohere_index",
                embeddings,
                allow_dangerous_deserialization=True
            )
            llm = ChatCohere(cohere_api_key=cohere_api,temperature=0.7)
            chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vectorIndex.as_retriever())
            result = chain({'question':query}, return_only_outputs=True)

            st.header("Answer")
            st.write(result['answer'])

            sources = result.get('sources', '')
            if sources:
                st.subheader("Sources")
                # source_list = [source.strip() for source in sources.split("\n") if source.strip()]
                source_list = sources.split('\n')
                for source in source_list:
                    st.write(f"• {source}")

        except Exception as e:
            st.error(f"Error loading vector DB or processing query: {str(e)}")
    else:
        st.warning("Please process URLs first to create the vector database.")
