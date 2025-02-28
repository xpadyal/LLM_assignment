from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from chunking import create_chunks
from notes import transcript

def init_vector_store() -> Chroma:
    """
    Initialize and return a Chroma vector store using transcript documents.
    """
    _, document_chunks, _ = create_chunks(transcript)
    embeddings = OpenAIEmbeddings()
    vector_store = Chroma.from_documents(
        documents=document_chunks,
        embedding=embeddings,
        collection_name="transcript-chunks"
    )
    return vector_store

def get_relevant_chunks(query: str, vector_store: Chroma, k: int = 3) -> str:
    """
    Retrieve relevant transcript chunks based on the query.
    """
    relevant_docs = vector_store.similarity_search(query, k=k)
    context = "\n".join([doc.page_content for doc in relevant_docs])
    return context
