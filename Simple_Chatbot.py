# Simple Chatbot V1.5
#🤖 Text-based conversational chatbot.

# Copyright (c) 2023, Sourceduty
# This software is free and open-source; anyone can redistribute it and/or modify it.

import random

# Define commands and replies as dictionaries for better organization
commands = {
    "greet": ["hello", "hi", "hey", "chatbot", "respond"],
    "leave": ["bye", "chatbot sleep", "goodbye"],
    "ask": ["name", "identify"],
    "sad": ["bad", "sad", "not feeling well", "unhappy", "depressed"],
    "happy": ["happy", "good", "joyful", "calm", "great", "amazing", "awesome"],
    "bored": ["boring", "bored", "bore", "nothing to do"],
    "food": ["hungry", "food", "eat", "dinner"],
    "weather": ["weather", "forecast", "temperature"]
}

replies = {
    "greet": ["Hello", "Greetings!", "How can chatbot help you?"],
    "leave": ["Goodbye", "Take care!", "See you later!"],
    "ask": ["My name is Chatbot", "I'm Chatbot, your virtual assistant."],
    "sad": ["I'm here to chat and cheer you up!", "Let's talk about something to make you feel better.", "I'm sorry to hear that. How can I help?"],
    "happy": ["I'm glad to hear that!", "What's making you feel so happy?", "That's fantastic!"],
    "bored": [
        "Watch some stand-up comedy videos.",
        "Install a new game.",
        "Try learning a new skill or hobby.",
        "Take a nap to recharge.",
        "How about reading a book?",
        "Explore a new hobby or craft project.",
        "Call or chat with a friend for some fun conversation."
    ],
    "food": [
        "What type of cuisine are you in the mood for?",
        "Cook something delicious at home or order your favorite takeout.",
        "I can suggest some recipes if you'd like!",
        "Eating a healthy meal can lift your spirits. What's your favorite dish?"
    ],
    "weather": ["I can provide you with the current weather for your location. Please share your city or zip code."]
}

# Create a function to get a random reply for a given command
def get_reply(command):
    return random.choice(replies.get(command, ["I don't understand that."]))

def chatbot(text):
    # Check for commands in the input text
    for key, command_list in commands.items():
        for word in text.split():
            if word in command_list:
                response = get_reply(key)
                print(response)
                return response

    print("Invalid entry.")
    return False

def number_guess_game():
    # ... (your existing number guessing game code remains unchanged)

def main():
    print("Simple Chatbot V1.2")
    print("---------------------------------")
    
    while True:
        print("1. Chat with the chatbot")
        print("2. Play a number guessing game")
        print("3. Quit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            print("You are now chatting with the chatbot.")
            print("Type 'exit' to return to the main menu.")
            while True:
                word = input().lower()
                if word == 'exit':
                    break
                chatbot(word)
        elif choice == '2':
            number_guess_game()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
