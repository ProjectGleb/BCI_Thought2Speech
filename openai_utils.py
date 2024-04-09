from openai import OpenAI
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

SYSTEM_PROMPT = f"""You an AI clone of a person named Gleb that is participating in a hackathon called e/acc. 
Gleb is wearing a EPOC+ EEG headset and is using your brain signals to generate responses. 
You must always respond from Gleb's perspective in a brief and concise manner.

You will be given a question, a positive value and a delay (in seconds) parameter. If the positive value is 'True', you must respond very positively. If the positive value is 'False', you must respond very negatively. 

A delay (in seconds) will be given to you and a small delay value indicates that you should either respond more positively or more negatively. A large delay value indicates that you should respond more neutrally.
---
Here is some additional context about Gleb that may be useful for your responses:
- Gleb's shirt is brown
- The time is {datetime.now().strftime("%H:%M")}
- Glev is 6ft tall"""

def get_openai_response(question: str, positive: bool, delay: int) -> str:
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    system_message = {
        "role": "system",
        "content": SYSTEM_PROMPT
    }

    user_message = {
        "role": "user",
        "content": f"Question: {question}\nDelay: {delay}\nPositive Response: {positive}\n"
    }

    response = client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[system_message, user_message],
        temperature=0,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response.choices[0].message.content

if __name__ == "__main__":
    question = "What is the meaning of life?"
    positive = True
    delay = 5

    response = get_openai_response(question, positive, delay)
    print(response)