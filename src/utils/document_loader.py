from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader,TextLoader

# Path of the documents directory
def load_documents(path):
    loader=DirectoryLoader(path,glob="*.pdf",loader_cls=PyPDFLoader) # ignore
    text_loader=DirectoryLoader(path,glob="*.txt",loader_cls=TextLoader)
    pdf_docs=loader.load()
    text_docs=text_loader.load()
    all_docs = pdf_docs + text_docs
    return all_docs



