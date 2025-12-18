from ..utils.document_loader import load_documents
from ..utils.logger import get_logger
logger = get_logger(__name__)




# Path of the documents directory
path=r"C:\Users\user\Desktop\Finance_RAG\documents"

documents = load_documents(path)
logger.info(f"Loaded {len(documents)} documents from {path}")

logger.info("Document loading completed.")



