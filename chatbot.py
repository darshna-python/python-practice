
print("ChatBot: Hello! I am your chatbot.")
print("Type 'bye' to exit.")

while True:
    user = input("You: ")

    if user.lower() == "hello":
        print("ChatBot: Hi Darshna!")

    elif user.lower() == "how are you":
        print("ChatBot: I am fine. Thanks for asking!")

    elif user.lower() == "what is your name":
        print("ChatBot: My name is Python Bot.")

    elif user.lower() == "bye":
        print("ChatBot: Goodbye!")
        break

    else:
        print("ChatBot: Sorry, I don't understand.")
