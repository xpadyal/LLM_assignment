from fastapi import FastAPI
from config import TITLE, VERSION, DESCRIPTION
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.responses import FileResponse
from endpoints import wrapped_chain
from langserve import add_routes
from middleware import add_cors
from notes import transcript, soap_note
import uvicorn
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()




app = FastAPI(
    title=TITLE,
    version=VERSION,
    description=DESCRIPTION
)

# Mount static directory
app.mount("/static", StaticFiles(directory="/static"), name="static")

# Serve the index.html file correctly
@app.get("/", response_class=FileResponse)
async def read_html():
    return FileResponse("/static/index.html")


#Fetch the notes(trnascript, soap notes)
add_routes(app, wrapped_chain, path="/ask")
@app.get("/notes")
async def get_notes():
    return {
        "transcript": transcript,
        "soap_note": soap_note
    }


add_cors(app)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)

