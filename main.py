import os
import streamlit as st
import speech_recognition as sr
import pyttsx3
from groq import Groq
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_token = os.getenv("GROQ_API_KEY")

# Initialize Groq API Client
client = Groq(api_key=api_token)

# Initialize TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Adjust speed if needed
engine.setProperty('volume', 1.0)  # Set volume level

# Streamlit app config
st.set_page_config(page_title="Tourist Chatbot", page_icon="🌍")
st.title("TouristUS ✈️ ")

# Define chatbot prompt template
template = """
You are a travel assistant chatbot named TouristUS, designed to help users plan trips.
Please provide detailed, informative, and engaging responses.

Chat history:
{chat_history}

User question:
{user_question} 
"""

prompt = ChatPromptTemplate.from_template(template)

# Function to get AI response from Groq
def get_response(user_query, chat_history):
    chat_input = prompt.format(chat_history=chat_history, user_question=user_query)

    response = client.chat.completions.create(
        model="llama3-8b-8192",  # Update model if needed
        messages=[{"role": "system", "content": chat_input}],
        temperature=0.7,
        max_tokens=500
    )

    return response.choices[0].message.content  # Extract AI response text

# Function for voice input
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎤 Speak now...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5)  # Listen for 5 seconds
            text = recognizer.recognize_google(audio)  # Convert speech to text
            st.success(f"✅ You said: {text}")
            return text
        except sr.UnknownValueError:
            st.error("❌ Could not understand the audio. Please try again.")
            return None
        except sr.RequestError:
            st.error("❌ Error with Speech Recognition service.")
            return None

# Function for voice output
import threading
def speak(text):
    def run_speech():
        engine.say(text)
        engine.runAndWait()

    threading.Thread(target=run_speech).start()

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [AIMessage(content="Hello, I am TouristUS! How can I assist you?")]

# Display chat history
for message in st.session_state.chat_history:
    with st.chat_message("AI" if isinstance(message, AIMessage) else "Human"):
        st.write(message.content)

# **Voice & Text Input Section**
col1, col2 = st.columns([1, 1])

# **Text Input**
with col1:
    user_query = st.text_input("Type your message:")

# **Voice Input**
with col2:
    if st.button("🎤 Speak"):
        user_query = recognize_speech()  # Capture speech and convert to text

if user_query:
    st.session_state.chat_history.append(HumanMessage(content=user_query))

    with st.chat_message("Human"):
        st.markdown(user_query)

    response = get_response(user_query, st.session_state.chat_history)

    with st.chat_message("AI"):
        st.write(response)

    # **Convert AI Response to Speech**
    speak(response)

    st.session_state.chat_history.append(AIMessage(content=response))