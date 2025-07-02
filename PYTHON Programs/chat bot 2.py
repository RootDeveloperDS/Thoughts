import google.generativeai as genai
import requests

# Set up the Gemini API key
genai.configure(api_key="API Key")

# Initialize the model
model = genai.GenerativeModel("gemini-2.0-flash")

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
        return response.text  # Extract text from the response
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