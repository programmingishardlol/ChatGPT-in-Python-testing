from openai import OpenAI

client = OpenAI(api_key="your key")

completion = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages = [{"role":"user", "content":"explain gravity"}]
)

print(completion.choices[0].message)