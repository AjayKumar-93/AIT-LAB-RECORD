import openai

# Set your API key (NOT recommended to hardcode in real applications)
openai.api_key = "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"

# Start the conversation setup
messages = []

# Ask user for chatbot personality
system_msg = input("What type of chatbot would you like to create?\n")
messages.append({"role": "system", "content": system_msg})

print("Your new assistant is ready! Type your query. Type 'quit()' to exit.\n")

# Chat loop
while True:
    user_input = input("You: ")
    
    if user_input.strip().lower() == "quit()":
        print("Exiting chatbot. Goodbye!")
        break

    messages.append({"role": "user", "content": user_input})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})

    print("\nAssistant:", reply, "\n")
