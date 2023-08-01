import requests
import re
from keywords import medical_terms

URL = "https://api.openai.com/v1/chat/completions"

# Your headers and other code remain unchanged
headers = { 
    "Authorization":"Bearer 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",
    "content-Type":"application/json",
}

def is_healthcare_question(question):
    question_words = re.findall(r'\b\w+\b', question.lower())
    for keyword in medical_terms:
        keyword_words = keyword.lower().split()
        for i in range(len(question_words) - len(keyword_words) + 1):
            if all(question_words[i + j] in keyword_words for j in range(len(keyword_words))):
                return True
    return False


def chatbot(prompt):
    data = {
        "model" : "gpt-3.5-turbo",
        "messages":[
            {"role":"system","content":"You are a kind helpful assistant"},
            {"role":"user","content":prompt}
            ],
        "temperature":0
    }

    if is_healthcare_question(prompt):
        response = requests.post(URL, headers=headers, json=data)
        response_data = response.json()
        return response_data['choices'][0]['message']['content']
    else:
        return "Apologies, please only share questions related to Health, medicine, or healthcare."

user_prompt = input("user : ")
response = chatbot(user_prompt)
print("ChatGPT : ", response)