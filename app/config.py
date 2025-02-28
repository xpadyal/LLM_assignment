import os
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv("HOST", "0.0.0.0")
# PORT = int(os.getenv("PORT", 10000))
TITLE = os.getenv("TITLE", "DeepScribe Chat API")
VERSION = os.getenv("VERSION", "1.0")
DESCRIPTION = os.getenv("DESCRIPTION", "API for querying patient transcripts using LangChain")
