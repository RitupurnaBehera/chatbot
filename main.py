import requests
import os



URL = "https://api.openai.com/v1/chat/completions"

api_key = os.environ.get("API_KEY")

if api_key is None:
    raise ValueError("API_KEY environment variable not set")

headers = { 
    "Authorization":f"Bearer {api_key}",
    "content-Type":"application/json",
}

def chatbot(prompt):

    data = {
        "model" : "gpt-3.5-turbo",
        "messages":[
            {"role":"system","content":"You are a kind helpful assistant"},
            {"role":"user","content":prompt}
            ],
        "temperature":0
    }

    response = requests.post(URL, headers=headers, json=data)
    response_data = response.json()
    return response_data['choices'][0]['message']['content']

user_prompt = input("user : ")
response = chatbot(user_prompt)
print("ChatGPT : ",response)


