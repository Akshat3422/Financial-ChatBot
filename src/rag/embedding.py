import os 
from dotenv import load_dotenv
from pinecone import Pinecone
from ..utils.chunk import chunk_documents
from ..utils.pinecone_initializer import initialize_pinecone
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings




load_dotenv()  # take environment variables from .env file




api_key = os.getenv("GOOGLE_API_KEY")
embedding=GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")

# Initialize Pinecone
index=initialize_pinecone(index_name=os.getenv("INDEX_NAME"))



def embed_and_store(documents):
    vectors = []

    chunks=chunk_documents(documents)
    for i, chunk in enumerate(chunks):
        vector = embedding.embed_documents([chunk.page_content])[0]  # extract the flat list
        vectors.append({
            "id": f"chunk-{i}",
            "values": vector,  # now a flat list
            "metadata": {
                "source": chunk.metadata.get("source", ""),
                "chunk_text": chunk.page_content
            }
        })
    return vectors

    # Upsert into Pinecone





