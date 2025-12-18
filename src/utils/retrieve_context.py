import os
from dotenv import load_dotenv
from langchain_pinecone import PineconeVectorStore
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from ..utils.pinecone_initializer import initialize_pinecone
from ...src.rag.retriever import get_retriever

load_dotenv()

embedding=GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
index=initialize_pinecone(index_name=os.getenv("INDEX_NAME"))

vectorstore = get_retriever()


def retrieve_context(query: str):
    """Retrieve information to help answer a query."""
    retrieved_docs = vectorstore.similarity_search(query, k=3) #ignore 
    serialized = "\n\n".join(
        (f"Source: {doc.metadata}\nContent: {doc.page_content}")
        for doc in retrieved_docs
    )
    return serialized, retrieved_docs
