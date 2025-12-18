from ..utils.document_loader import load_documents
from ..utils.logger import get_logger
from ..utils.chunk import chunk_documents




logger = get_logger(__name__)
# Path of the documents directory
path=r"C:\Users\user\Desktop\Finance_RAG\documents"

documents = load_documents(path)
chunks = chunk_documents(documents)

logger.info(f"Loaded {len(documents)} documents from {path}")

logger.info(f"Chunked documents into {len(chunks)} chunks.")



