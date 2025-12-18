import os
from dotenv import load_dotenv
from langchain_pinecone import PineconeVectorStore
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from ..utils.pinecone_initializer import initialize_pinecone


load_dotenv()


embedding=GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
index=initialize_pinecone(index_name=os.getenv("INDEX_NAME"))



def get_retriever(index=index,embedding=embedding):

    vectorstore =PineconeVectorStore(
        index=index,
        embedding=embedding,
        text_key="chunk_text"
    )
    retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

    return retriever