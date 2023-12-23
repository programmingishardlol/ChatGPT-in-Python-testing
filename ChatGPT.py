from openai import OpenAI

class chatgpt:
    def __init__(self):
        self.messages = []
        self.client = OpenAI(api_key="your key")

    def generate(self, user_input):

        # add user input to messages
        self.messages.append({"role":"user", "content":user_input})
        response = self.client.chat.completions.create(
            model = "gpt-3.5-turbo",
            messages = self.messages
        )
        # get gpt output
        reply = response["choices"][0]["message"]["content"]
        # ai memorization
        self.messages.append({"role":"assistant", "content":reply})
        print(reply)

def main():
    gpt = chatgpt()
    print("Hi, what can i help you")

    # repeating asking questions
    while input != "q":
        gpt.generate(input())
    print("Have a great time")

main()
