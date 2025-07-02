import google.generativeai as genai

genai.configure(api_key="api key")  # Replace with YOUR actual API key

try:
    model = genai.GenerativeModel("gemini-1.0-pro")
    print("Gemini 1.0 Pro is accessible!")
except Exception as e:
    print(f"Gemini 1.0 Pro is NOT accessible: {e}")
try:
    model = genai.GenerativeModel("gemini-1.5-pro")  # If you suspect you might have access
    print("Gemini 1.5 Pro is accessible!")
except Exception as e:
    print(f"Gemini 1.5 Pro is NOT accessible: {e}")
    
try:
    model = genai.GenerativeModel("gemini-2.0-pro")  # If you suspect you might have access
    print("Gemini 2.0 Pro is accessible!")
except Exception as e:
    print(f"Gemini 2.0 Pro is NOT accessible: {e}")
print("Chatbot: Hello! Type 'exit' to end the chat.")

while True:
"""   if not check_internet():
        print("Chatbot: No internet connection. Please check your network and try again.")
        break"""

    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    response = chatbot_response(user_input)
    print("Chatbot:", response)