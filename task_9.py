import openai

# Warning: Never expose your key in code like this!
openai.api_key = "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"

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{
        "role": "user",
        "content": "Give me 3 ideas that I could build using OpenAI APIs"
    }]
)

print(completion.choices[0].message.content)
