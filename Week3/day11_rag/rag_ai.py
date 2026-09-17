import os 
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv();
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("api key incorrect")

client=Groq(api_key=my_api_key)
model="Qwen/Qwen3.8-27B"

#step1
knowledge_base={
    "hobbies": "chess, cricket, football",
    "movies": "interstellar, inception, tenet",
    "name": "christop lan",
    "age": "christop lan age is 50 years"
}

def retrieve_info(question):
    question=question.lower()
    if "age" in question:
        return knowledge_base["age"]
    elif "movies" in question:
        return knowledge_base["movies"]
    elif "name" in question:
        return knowledge_base["name"]
    else:
        return knowledge_base["hobbies"]


def ask_llm(question):
    context=retrieve_info(question)

    sys_prompt=f"""
    answer in one line only. Answer only based on this context. Don't hallucinate. Context: {context}
    """    
    system_message={
        "role":"system",
        "content":sys_prompt
    }
    message={
        "role":"user",
        "content":question
    }

    messages=[system_message, message]
    response=client.chat.completions.create(model=model, messages=messages)
    answer=response.choices[0].message.content
    return answer

question="what is age?"
print(ask_llm(question))