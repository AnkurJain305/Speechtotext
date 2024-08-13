import streamlit as st
import speech_recognition as sr
from pydub import AudioSegment
from pydub.playback import play

st.title("Speech-to-Text Example")

if st.button("Record"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Recording...")
        audio = recognizer.listen(source,timeout=10,phrase_time_limit=30)
        st.write("Recording complete.")
        
        try:
            text = recognizer.recognize_google(audio)
            st.write(f"Transcription: {text}")
        except sr.UnknownValueError:
            st.write("Could not understand audio.")
        except sr.RequestError as e:
            st.write(f"Could not request results; {e}")

