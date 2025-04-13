import google.generativeai as genai
import requests

# Set up the Gemini API key
genai.configure(api_key="AIzaSyAu9ylboEmEZkgMjAZ1dLUbI8BsYUavH_M")

# Initialize the model
model = genai.GenerativeModel("Generative Language API Key")

# Function to check internet connection
def check_internet():
    try:
        requests.get("https://www.google.com", timeout=5)  # Ping Google
        return True
    except requests.ConnectionError:
        return False

def chatbot_response(user_input):
    try:
        response = model.generate_content(user_input)
        return response.candidates[0].content if response.candidates else "No response from model."
    except Exception as e:
        return f"Error: {str(e)}"

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
        break

    response = chatbot_response(user_input)
    print("Chatbot:", response)