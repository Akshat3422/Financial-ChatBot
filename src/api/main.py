from ..rag.rag_pipeline import generate_answer

# RAG
query = "What must lenders communicate to small borrowers if a loan application up to Rs. 2 lakhs is rejected?"


answer, docs = generate_answer(query)
print("Answer:", answer)