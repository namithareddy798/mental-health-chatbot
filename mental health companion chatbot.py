import random
import datetime
import json

# Predefined responses
responses = {
    "sad": [
        "I'm really sorry you're feeling sad. 💙 You're not alone.",
        "It's okay to feel sad sometimes. Would you like to talk about it?",
        "Remember, tough times don't last forever."
    ],
    "anxious": [
        "Take a deep breath. Inhale... Exhale... 🌿",
        "Anxiety can feel overwhelming, but you are stronger than it.",
        "Try a short 2-minute breathing exercise."
    ],
    "happy": [
        "That's wonderful to hear! 😊",
        "I'm glad you're feeling happy today!",
        "Keep spreading positivity!"
    ],
    "angry": [
        "It's okay to feel angry. Let's try calming down together.",
        "Take a moment to breathe before reacting.",
        "Would you like to try a quick relaxation tip?"
    ],
    "default": [
        "I'm here for you. Tell me more.",
        "That sounds important. Would you like to share more?",
        "I understand. Please continue."
    ]
}

# Emergency keywords
emergency_words = ["suicide", "kill myself", "end my life", "die"]

# Mood detection function
def detect_mood(user_input):
    user_input = user_input.lower()
    
    if any(word in user_input for word in ["sad", "depressed", "unhappy", "cry"]):
        return "sad"
    elif any(word in user_input for word in ["anxious", "worried", "nervous", "stress"]):
        return "anxious"
    elif any(word in user_input for word in ["happy", "good", "great", "excited"]):
        return "happy"
    elif any(word in user_input for word in ["angry", "mad", "furious"]):
        return "angry"
    elif any(word in user_input for word in emergency_words):
        return "emergency"
    else:
        return "default"

# Save chat history
def save_chat(user_input, bot_response):
    chat_data = {
        "time": str(datetime.datetime.now()),
        "user": user_input,
        "bot": bot_response
    }
    
    try:
        with open("chat_history.json", "a") as file:
            file.write(json.dumps(chat_data) + "\n")
    except:
        pass

# Chatbot main function
def chatbot():
    print("🧠 Mental Health Companion Chatbot")
    print("Type 'exit' to end the chat.\n")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "exit":
            print("Bot: Take care! Remember, you are valued and important. 💙")
            break
        
        mood = detect_mood(user_input)
        
        if mood == "emergency":
            bot_response = "⚠️ It sounds like you're going through something very serious. Please contact a mental health professional or call your local emergency helpline immediately."
        else:
            bot_response = random.choice(responses[mood])
        
        print("Bot:", bot_response)
        save_chat(user_input, bot_response)

# Run chatbot
if __name__ == "__main__":
    chatbot()