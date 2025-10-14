import openai
import gradio as gr

# WARNING: Don't hardcode API keys in production
openai.api_key = "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"

# Initial system message to guide the assistant's personality
messages = [
    {
        "role": "system",
        "content": "You are a financial expert that specializes in real estate investment and negotiation."
    }
]

# Define the chatbot function
def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    return reply

# Create Gradio interface
demo = gr.Interface(
    fn=CustomChatGPT,
    inputs="text",
    outputs="text",
    title="INTELLIGENT CHATBOT - Real Estate Advisor"
)

# Launch Gradio app with a public share link
demo.launch(share=True)
