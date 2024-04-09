import streamlit as st
import json
import requests
from streamlit_lottie import st_lottie
import time
from datetime import datetime
from dateutil.parser import parse
import pytz
import supabase_api
from openai_utils import get_openai_response
from elevenlabs_utils import generate_audio, generate_cloned_audio
import base64
from dotenv import load_dotenv
from datetime import timedelta
import os

load_dotenv()

# Utility functions
def autoplay_audio(file_path: str):
    """Autoplays audio file."""
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio controls autoplay="true">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(
            md,
            unsafe_allow_html=True,
        )

def load_lottiefile(filepath: str):
    """Loads lottie file."""
    with open(filepath, "r") as file:
        return json.load(file)

def get_latest_response(question_time):
    """Gets the latest response from the database that is newer than the question time."""
    while True:
        latest_response = supabase_api.get_last_response_from_database()
        if latest_response:
            response_time = parse(latest_response['created_at'])
            if response_time - question_time >= timedelta(seconds=3):
                return latest_response
        time.sleep(1)

def handle_response(question, latest_response, question_time):
    """Handles the response from the database."""
    answer = latest_response['response']
    delay = (parse(latest_response['created_at']) - question_time).total_seconds()
    response = get_openai_response(question, answer == "yes", delay)
    audio = generate_audio(response)
    with open("temp.mp3", "wb") as f:
        f.write(audio)
    lottie_animation = load_lottiefile("lottie_files/siri-sound-wave.json")
    st_lottie(lottie_animation, speed=1, width=800, height=400, key="animation")
    autoplay_audio("temp.mp3")
    # Delete the temp.mp3 file
    os.remove("temp.mp3")
    # st.write("[DEBUG] Answer:", response)

def main():
    st.title("Mindspeak: EEG Response App")

    question = st.text_input("Enter your question:")

    if st.button("Submit"):
        question_time = datetime.now(pytz.UTC)

        # Use st.spinner to show a loading spinner and message while waiting for a response
        with st.spinner('Waiting for an answer...'):
            latest_response = get_latest_response(question_time)

        # Show an indication that we have received a response from the EEG headset
        st.success('Received a signal from the EEG headset, processing response...')
        
        latest_response = get_latest_response(question_time)
        handle_response(question, latest_response, question_time)

if __name__ == "__main__":
    main()