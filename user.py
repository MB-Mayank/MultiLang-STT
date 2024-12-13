import streamlit as st
import requests

# Streamlit UI for audio file upload
st.title("Multilingula Speech Recognition with Whisper")
st.subheader("Upload an audio file to get its STT")

uploaded_file = st.file_uploader("Choose an audio file", type=["mp3"])

if uploaded_file:
    # Display upload success
    st.info("File uploaded successfully!")

    # Send file to FastAPI for processing
    with st.spinner("Processing..."):
        response = requests.post(
            "http://127.0.0.1:8000/upload",  # Replace with your FastAPI endpoint
            files={"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}
        )

    # Handle API response
    if response.status_code == 200:
        st.success("STT complete!")
        st.text_area("STT:", value=response.json()["transcription"], height=300)
    else:
        st.error(f"Error: {response.json()['detail']}")
