from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from notes import soap_note
from vector_store import get_relevant_chunks, init_vector_store

# Initialize the model and vector store.
model = ChatGroq(model="llama3-70B-8192", temperature=0.2)
vector_store = init_vector_store()


# Process the incoming chat messages using a custom chain.
def custom_chain(messages: list) -> dict:
    query = messages[-1]["content"]
    dynamic_context = get_relevant_chunks(query, vector_store)

    system_template = """
    You are a medical assistant helping providers answer questions about a patient. 
    Use ONLY the following transcript and SOAP note.
    Intelligently bold the important information if the user asks for a particular information(Do not bold the whole sentence but only words).
    Also, you can ask for follow-up questions if the query is not specific or clear based on your own understanding.
    If information isn't present then gracefully decline to answer the user's question.

    Transcript:
    {context}

    SOAP Note:
    {soap_note}

    Answer concisely in 1-2 sentences. Do not speculate."""
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_template),
        MessagesPlaceholder(variable_name="messages")
    ])

    inputs = {
        "messages": messages,
        "context": dynamic_context,
        "soap_note": soap_note,
    }

    # Compose the chain by piping the prompt to the model
    chain = prompt | model
    result = chain.invoke(inputs)
    response_str = result.content if hasattr(result, "content") else str(result)

    return {"output": {"content": response_str}}
