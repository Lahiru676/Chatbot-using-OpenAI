from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
client = OpenAI()
while True:
    question = input("user:")
    if question != "bye":

        response = client.chat.completions.create(
            model="gpt-3.5-turbo", 
            max_tokens=50,# max number of tokens in the generated response
            n = 1,# number of generated responses
            temperature=0.7,# temperature controls the randomness of the generated response   
            messages=[{"role": "user", "content": question}])

        for choice in response.choices:
            print(f"AI :{choice.message.content}")
    else:
        print("AI: bye.")
        break


