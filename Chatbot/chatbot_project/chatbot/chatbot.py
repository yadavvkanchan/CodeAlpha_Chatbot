# chatbot/chatbot.py

import nltk
import random
import string
from nltk.chat.util import Chat, reflections

# Download NLTK resources (if not done already)
nltk.download('punkt')
nltk.download('stopwords')

# Define some patterns and responses for the chatbot
patterns_responses = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you?', ['I\'m doing well, thank you!', 'I\'m great, thanks for asking!']),
    (r'what is your name?', ['I am a chatbot. What can I do for you?']),
    (r'quit', ['Goodbye! Have a nice day!']),
    (r'(.*) (your|you) (.*)', ['I\'m just a chatbot, but I\'m happy to help!']),
    (r'(.*)', ['I\'m not sure how to respond to that. Can you ask something else?'])
]

# Create chatbot instance
chatbot = Chat(patterns_responses, reflections)

def get_response(user_input):
    # Clean user input and get response
    user_input = user_input.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    return chatbot.respond(user_input)
