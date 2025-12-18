import os 
from dotenv import load_dotenv
from pinecone import Pinecone


load_dotenv()
def initialize_pinecone():
    pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

    index_name = "vectordb"

# Check if index exists
    if not pc.has_index(index_name):
        pc.create_index_for_model(
        name=index_name,
        cloud="aws",
        region="us-east-1",
        embed={"model": "llama-text-embed-v2",
            "field_map": {"text": "chunk_text"}
        } # type: ignore
    )
        return pc.Index(index_name)
        

