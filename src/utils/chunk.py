from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_documents(all_docs, chunk_size=500, chunk_overlap=100):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    chunks = splitter.split_documents(all_docs)
    return chunks
