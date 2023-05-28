import openai
while True:
    openai.api_key = 'Your api key'

# Define the prompt for the text generation
    prompt = input("I am PS4:")

# Generate text using OpenAI's GPT-3.5 model
    response = openai.Completion.create(
        engine="text-davinci-003",  # GPT-3.5 model
        prompt=prompt,
        max_tokens=100  # Number of tokens to generate
    )

# Print the generated text
    print(response.choices[0].text)
