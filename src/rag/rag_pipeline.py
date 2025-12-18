
from langchain_groq import ChatGroq
from ..utils.retrieve_context import retrieve_context
from ..llm.prompt_templates import prompt # type: ignore


# LLM
chat_model = ChatGroq(model="llama-3.3-70b-versatile",temperature=2)

def generate_answer(query: str):
    context, docs = retrieve_context(query)
# Create messages
    messages = prompt.invoke({
        "context": context,
        "question": query
    })
# Invoke model
    answer = chat_model.invoke(messages)
    return answer, docs
