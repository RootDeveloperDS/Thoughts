import google.generativeai as genai

# Set up the Gemini API key
genai.configure(api_key="AIzaSyAu9ylboEmEZkgMjAZ1dLUbI8BsYUavH_M")

# Initialize the model
model = genai.GenerativeModel("gemini-pro")

def chatbot_response(user_input):
    response = model.generate_content(user_input)
    return response.text  # Extract text from the response

print("Chatbot: Hello! Type 'exit' to end the chat.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)
