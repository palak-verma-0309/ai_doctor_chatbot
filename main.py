import google.generativeai as genai

genai.configure(api_key="AIzaSyALQUcmdl87erB8wXPZnQCSO1DQDq-H9Vs")

model = genai.GenerativeModel("models/gemini-2.0-flash")

chat = model.start_chat()

print("Doctor Bot: Hello! I'm Dr. AI. How can I assist you today?")

while True:
    user_input = input(" You: ")
    
    if user_input.lower() in ["exit", "quit", "bye"]:
        print(" Doctor Bot: Take care! Wishing you good health. ")
        break
    response = chat.send_message(f"You're a helpful and experienced doctor. Answer politely. User says: {user_input}")
    print("Doctor Bot:", response.text)