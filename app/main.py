from fastapi import FastAPI
from config import TITLE, VERSION, DESCRIPTION, HOST, PORT
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from endpoints import wrapped_chain
from langserve import add_routes
from middleware import add_cors
from notes import transcript, soap_note
import uvicorn


app = FastAPI(
    title=TITLE,
    version=VERSION,
    description=DESCRIPTION
)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/") 
def serve_frontend():
    return FileResponse("static/index.html")


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
      # Render dynamically sets PORT
    uvicorn.run("main:app", host="0.0.0.0", port=PORT, reload=False)
