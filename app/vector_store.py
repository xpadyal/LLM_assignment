from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from chunking import create_chunks
from notes import transcript

# Initialize and return a Chroma vector store.
def init_vector_store() -> Chroma:
    
    _, document_chunks, _ = create_chunks(transcript)
    embeddings = OpenAIEmbeddings()
    vector_store = Chroma.from_documents(
        documents=document_chunks,
        embedding=embeddings,
        collection_name="transcript-chunks"
    )
    return vector_store


#Retrieve relevant transcript chunks based on the query.
def get_relevant_chunks(query: str, vector_store: Chroma, k: int = 3) -> str:
    
    relevant_docs = vector_store.similarity_search(query, k=k)
    context = "\n".join([doc.page_content for doc in relevant_docs])
    return context
