def simple_chatbot():
    print("Bot: Hello! I'm your simple chatbot. Type 'bye' to end the chat.")
    
    while True:
        user_input = input("You: ").lower()

        if "hello" in user_input or "hi" in user_input:
            print("Bot: Hello there! How can I help you today?")

        elif "how are you" in user_input:
            print("Bot: I'm just a program, but I'm doing great! How about you?")

        elif "your name" in user_input:
            print("Bot: I'm a simple chatbot created by user")

        elif "help" in user_input:
            print("Bot: Sure! I can answer basic questions or just chat with you.")

        elif "bye" in user_input or "exit" in user_input:
            print("Bot: Goodbye! Have a great day!")
            break

        else:
            print("Bot: I'm not sure how to respond to that. Can you rephrase?")

# Run the chatbot
simple_chatbot()
