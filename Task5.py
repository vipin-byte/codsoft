import random

def chatbot_response(user_input):
    responses = {
        "hello": ["Hi there!", "Hello!", "Hey! How can I help you?"],
        "how are you": ["I'm just a program, but I'm doing great!", "I'm fine, thank you!", "All systems operational!"],
        "bye": ["Goodbye!", "See you later!", "Take care!"],
        "default": ["I'm sorry, I don't understand that.", "Can you rephrase?", "I'm here to help!"]
    }

    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(responses["default"])

def main():
    print("Chatbot: Hi! I'm your chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if "bye" in user_input.lower():
            print("Chatbot: Goodbye!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()