from ..utils.document_loader import load_documents
from ..utils.logger import get_logger
from langchain_text_splitters import RecursiveCharacterTextSplitter




logger = get_logger(__name__)
# Path of the documents directory

def chunk_documents(all_docs, chunk_size=500, chunk_overlap=100):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    chunks = splitter.split_documents(all_docs)
    return chunks


logger.info(f"Chunked documents into   chunks.")



