

def get_reply(user_message):
    # Convert to lowercase so "Hello" and "hello" both work
    user_message = user_message.lower()

    if user_message == "hello" or user_message == "hi":
        return "Hi! How can I help you?"

    elif user_message == "how are you":
        return "I'm fine, thanks! How about you?"

    elif user_message == "bye" or user_message == "goodbye":
        return "Goodbye! Have a nice day!"

    elif user_message == "what is your name":
        return "I am a simple chatbot made in Python!"

    elif user_message == "what can you do":
        return "I can reply to basic messages like hello, bye, how are you!"

    else:
        return "Sorry, I don't understand that. Try: hello, how are you, bye"


# Main loop
def start_chatbot():
    print("=" * 40)
    print("      Welcome to Simple Chatbot!")
    print("   Type 'bye' to exit the chatbot.")
    print("=" * 40)

    while True:
        # Take input from user
        user_input = input("\nYou: ")

        # If user types nothing, ask again
        if user_input.strip() == "":
            print("Bot: Please type something!")
            continue

        # Get the bot's reply
        reply = get_reply(user_input)
        print("Bot:", reply)

        # Stop the loop if user says bye
        if user_input.lower() in ["bye", "goodbye"]:
            break


# Start the chatbot
start_chatbot()