### README.md

# MultiLang-Speech to text

This project provides an **AI-powered transcription service** that converts audio files into text using OpenAI's Whisper model. It includes two components:  
1. A **FastAPI backend** (`app.py`) for audio processing and transcription.  
2. A **Streamlit frontend** (`user.py`) for user interaction.

---

## Features
- Upload audio files in `.mp3` format for transcription.
- Real-time transcription powered by the Whisper model.
- User-friendly web interface with Streamlit.
- Scalable API built with FastAPI.

---

## Requirements

### Prerequisites
Before running the project, ensure you have the following installed:
- Python 3.8 or above
- Required Python libraries (see below)

### Install Dependencies
1. Clone this repository:
   ```bash
   git clone https://github.com/MB-Mayank/MultiLang-STT/tree/58d1198d1a63634bebfe22e9d16074f79a3e8f55
   cd MultiLang-STT
   ```
2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

**Sample `requirements.txt`:**
```plaintext
fastapi
uvicorn
streamlit
requests
whisper
```

3. Install **Whisper**:
   ```bash
   pip install git+https://github.com/openai/whisper.git
   ```

4. Install **FFmpeg** (required by Whisper):
   - On Linux:
     ```bash
     sudo apt update && sudo apt install ffmpeg
     ```
   - On macOS:
     ```bash
     brew install ffmpeg
     ```
   - On Windows: Download FFmpeg binaries from [FFmpeg.org](https://ffmpeg.org/download.html) and add it to your PATH.

---

## How to Run

### 1. Start the FastAPI Backend
1. Navigate to the directory containing `app.py`.
2. Run the FastAPI app:
   ```bash
   uvicorn app:app --reload
   ```
3. The API will be available at: `http://127.0.0.1:8000`.

### 2. Run the Streamlit Frontend
1. Open a new terminal window.
2. Navigate to the directory containing `user.py`.
3. Start the Streamlit app:
   ```bash
   streamlit run user.py
   ```
4. Open the Streamlit interface in your browser`.

---

## API Endpoints

### Health Check
- **GET** `/`
  - Returns: `{"message": "Welcome to the Whisper Transcription API!"}`

### Upload Audio and Transcribe
- **POST** `/upload`
  - **Request**: An audio file in `.mp3` format.
  - **Response**:
    ```json
    {
      "message": "File processed successfully!",
      "transcription": "<transcribed text>"
    }
    ```

---

## How to Use

1. Open the Streamlit web app.
2. Upload an audio file in `.mp3` format.
3. Wait for the transcription to process.
4. View and copy the transcription from the interface.

---

## Troubleshooting

- **Error: "Invalid file type"**: Ensure the uploaded file is an audio file in `.mp3` format.
- **Whisper model not found**: Make sure you have installed the Whisper library correctly.
- **FFmpeg not found**: Ensure FFmpeg is installed and accessible in your system PATH.

---

