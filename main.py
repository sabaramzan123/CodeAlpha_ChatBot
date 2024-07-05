import spacy
import random
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download NLTK's VADER sentiment analyzer
nltk.download('vader_lexicon')

# Initialize spaCy and NLTK
nlp = spacy.load("en_core_web_sm")
sid = SentimentIntensityAnalyzer()

# Predefined responses and additional information
responses = {
    "hi": ["Hello! How can I assist you today?", "Hi there! How's it going?", "Hey! What's up?"],
    "hello": ["Hi! What can I do for you?", "Hey! How can I help?", "Hello there! How can I assist you?"],
    "how are you?": ["I'm just a bot, but I'm here to help!", "I'm doing well, thank you! How about you?", "I'm great, thanks for asking! How are you?"],
    "what is your name?": ["I'm a chatbot created to assist you.", "You can call me Chatbot!", "I'm your friendly assistant, Chatbot."],
    "tell me a joke": [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why was the math book sad? Because it had too many problems!",
        "Why don't skeletons fight each other? They don't have the guts!"
    ],
    "what can you do?": [
        "I can chat with you, answer questions, and provide information.",
        "I can tell you jokes, give you information, and chat with you!",
        "I'm here to assist you with any questions you might have."
    ],
    "what is the weather like?": [
        "I'm not sure, but you can check a weather app for accurate information.",
        "I don't have real-time weather data, but it's always good to check online!",
        "Weather can change quickly, so it's best to check a reliable weather source."
    ],
    "tell me a fun fact": [
        "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old and still edible!",
        "A group of flamingos is called a 'flamboyance'!",
        "Octopuses have three hearts!"
    ],
    "how old are you?": ["I'm ageless!", "I exist outside of time.", "Age is just a number for me!"],
    "what is your favorite color?": ["I like all colors equally!", "I don't have a favorite color, but I appreciate the beauty of all colors.", "Colors are wonderful, aren't they?"],
    "who created you?": ["I was created by developers using natural language processing techniques.", "I was designed by a team of skilled programmers.", "My creators are the brilliant minds behind this technology."],
    "default": ["I'm not sure I understand. Can you rephrase?", "Can you tell me more about that?", "I'm not quite sure what you mean. Could you explain further?"]
}

# Function to get a response based on user input
def get_response(user_input):
    # Process the user input with spaCy
    doc = nlp(user_input)
    
    # Extract entities from the user input
    entities = [ent.text for ent in doc.ents]

    # Choose a response based on predefined responses or default
    user_input_lower = user_input.lower()
    response = random.choice(responses.get(user_input_lower, responses["default"]))
    
    # Add information about entities if present
    if entities:
        response += " I see you mentioned: " + ", ".join(entities) + "."
    
    return response

# Function to start a conversation with the chatbot
def chat():
    print("Hello! I'm your chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("Saba: ")
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chat()
