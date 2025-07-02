import google.generativeai as genai
import requests
import gtts  # Google Text-to-Speech
import os

# Set up the Gemini API key
genai.configure(api_key="api key")

# Initialize the model
model = genai.GenerativeModel("gemini-2.0-flash")

# Function to check internet connection
def check_internet():
    try:
        requests.get("https://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

# Function to get AI response
def chatbot_response(user_input):
    try:
        response = model.generate_content(user_input)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# Function to speak using gTTS and play using termux-media-player
def speak(text):
    tts = gtts.gTTS(text, lang="en")
    filename = "response.mp3"
    tts.save(filename)
    os.system(f"termux-media-player play {filename}")  # Use Termux media player to play sound

# Check internet before starting
if not check_internet():
    print("Chatbot: No internet connection. Please check your network and try again.")
    exit()

print("Chatbot: Hello! Type 'exit' to end the chat.")

while True:
    if not check_internet():
        print("Chatbot: No internet connection. Please check your network and try again.")
        break

    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        speak("Goodbye!")
        break

    response = chatbot_response(user_input)
    print("Chatbot:", response)
    speak(response)