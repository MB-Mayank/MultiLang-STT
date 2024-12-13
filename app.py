from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import os
import tempfile
import whisper
import subprocess

# Initialize FastAPI app
app = FastAPI()

# Load Whisper model
model = whisper.load_model("small")  # You can use 'tiny', 'small', 'medium', 'large' based on your needs

# Endpoint to upload and transcribe audio
@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        # Ensure the uploaded file is an audio file
        if not file.content_type.startswith("audio"):
            raise HTTPException(status_code=400, detail="Invalid file type. Please upload an audio file.")

        # Save the uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp:
            temp.write(await file.read())
            temp_path = temp.name

        # Transcribe the audio using Whisper
        transcription = model.transcribe(temp_path)

        # Clean up the temporary file
        os.remove(temp_path)

        # Return the transcription
        return JSONResponse(content={
            "message": "File processed successfully!",
            "transcription": transcription.get("text", "")
        })

    except Exception as e:
        # Handle errors and cleanup if necessary
        if 'temp_path' in locals() and os.path.exists(temp_path):
            os.remove(temp_path)
        raise HTTPException(status_code=500, detail=str(e))

# Health check endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Whisper Transcription API!"}