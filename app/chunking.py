import hashlib
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

def create_chunks(transcript_text: str, chunk_size: int = 1000, chunk_overlap: int = 200) -> tuple:
    """
    Split the transcript into chunks and return:
      - A list of raw text chunks,
      - A list of Document objects,
      - A list of dictionaries containing chunk id and content.
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ". ", "! ", "? ", " ", ""]
    )
    transcript_chunks = text_splitter.split_text(transcript_text)
    document_chunks = [Document(page_content=chunk) for chunk in transcript_chunks]

    chunk_data = []
    for chunk in transcript_chunks:
        chunk_id = hashlib.md5(chunk.encode()).hexdigest()
        chunk_data.append({
            "id": chunk_id,
            "content": chunk
        })

    return transcript_chunks, document_chunks, chunk_data
