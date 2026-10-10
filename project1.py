# ==========================================
# RULE-BASED AI CHATBOT - VERSION 2.0
# DecodeLabs Project 1
# ==========================================

def show_welcome():
    print("=" * 45)
    print("Welcome to My AI Chatbot!")
    print("=" * 45)
    print("I am a rule-based chatbot.")
    print("Type 'help' to see what I can do.")
    print("Type 'bye', 'exit', or 'quit' to leave.")
    print()


def show_help():
    print("\nAvailable Commands:")
    print("- hello / hi / hey")
    print("- how are you")
    print("- what is your name")
    print("- what can you do")
    print("- help")
    print("- thanks / thank you")
    print("- bye / exit / quit")
    print()


def chatbot_response(message):
    
    # Greetings
    if message in ["hello", "hi", "hey", "salam"]:
        return "Hello! Nice to meet you."

    # Feelings
    elif message in ["how are you", "how are you doing"]:
        return "I'm doing great! Thanks for asking."

    # Name
    elif message in ["what is your name", "your name"]:
        return "I'm a Rule-Based AI Chatbot."

    # Capabilities
    elif message in ["what can you do", "what do you do"]:
        return "I can respond to predefined messages using rules."

    # Thanks
    elif message in ["thanks", "thank you", "thankyou"]:
        return "You're welcome! "

    # Help
    elif message == "help":
        show_help()
        return None

    # Exit
    elif message in ["bye", "exit", "quit"]:
        return "EXIT"

    # Unknown input
    else:
        return "Sorry, I don't understand that yet."


# ==========================================
# MAIN PROGRAM
# ==========================================

show_welcome()

conversation_count = 0

while True:

    user_input = input("You: ")

    # Normalize input
    message = user_input.lower().strip()

    # Ignore empty input
    if message == "":
        print("Bot: Please type something.")
        continue

    conversation_count += 1

    response = chatbot_response(message)

    # Exit condition
    if response == "EXIT":
        print("Bot: Goodbye! ")
        print(f"Bot: You had {conversation_count} interactions with me.")
        break

    # Print normal response
    if response is not None:
        print("Bot:", response)