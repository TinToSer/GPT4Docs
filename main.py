import box
import timeit
import yaml
from src.utils import setup_dbqa
import os, streamlit as st
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.embeddings import HuggingFaceEmbeddings


with open(r'config\config.yml', 'r', encoding='utf8') as ymlfile:
    cfg = box.Box(yaml.safe_load(ymlfile))


# Define a simple Streamlit app
st.title("**GPT4Docs**")

if st.button("Rebuild VectorDB"):
    st.write("Building database ...")
    loader = DirectoryLoader(cfg.DATA_PATH,
                             glob='*.pdf',
                             loader_cls=PyPDFLoader)
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=cfg.CHUNK_SIZE,
                                                   chunk_overlap=cfg.CHUNK_OVERLAP)
    texts = text_splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2',
                                       model_kwargs={'device': 'cpu'})

    vectorstore = FAISS.from_documents(texts, embeddings)
    vectorstore.save_local(cfg.DB_FAISS_PATH)
    st.success("Database build completed ...")

model_list = [fli for fli in os.listdir(cfg.MODEL_BIN_DIR) if fli.endswith('.bin') ]    
model = st.selectbox("Select LLM model",model_list)
query = st.text_input("Just Ask?", "")
# If the 'Submit' button is clicked
if st.button("Submit"):
    if not query.strip():
        st.error(f"Please provide the search query.")
    else:
        try:
            # Setup DBQA
            conclusion=""
            start = timeit.default_timer()
            dbqa = setup_dbqa(model)
            response = dbqa({'query': query})
            end = timeit.default_timer()

            conclusion=conclusion+f'\nAnswer: {response["result"]}\n\n'

            # Process source documents
            source_docs = response['source_documents']
            for i, doc in enumerate(source_docs):
                conclusion=conclusion+f'\nSource Document {i+1}\n'
                conclusion=conclusion+f'\nSource Text: {doc.page_content}'
                conclusion=conclusion+f'\nDocument Name: {doc.metadata["source"]}'
                conclusion=conclusion+f'\nPage Number: {doc.metadata["page"]}\n\n'
                
            conclusion=conclusion+f"Time to retrieve response: {end - start}"
            st.success(conclusion)
            
        except Exception as e:
            st.error(f"An error occurred: {e}")


