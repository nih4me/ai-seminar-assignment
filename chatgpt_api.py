import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

# Setting ChatGPT context
jokes_expert = {
    "role": "system", 
    "content": "You are a jokes expert."
}

def invoke_chatgpt_for_jokes_explaination(joke, context=jokes_expert):
    prompt = [context]
    if joke:
        prompt.append(
            {
                "role": "user", 
                "content": f'Why is the following a joke ? {joke}'
            },
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=prompt
        )
      
        explainantion = chat.choices[0].message.content
        return explainantion