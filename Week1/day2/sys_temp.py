import os 
from pathlib import Path 
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key =os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("Api key error")

client = Groq(api_key=my_api_key)

model="llama-3.3-70b-versatile"
role="user"
# prompt="Go to hell"
prompt = "suggest a name for my food brand, suggest one name only"

# message_system={
#     "role":"system",
#     "content":"you are my strict professor who gets angry easily"
# } 

message_system={
    "role":"system",
    "content": "you are a brand manager who has expertise with managing food brands"
}

message={
    "role":role,
    "content":prompt
}

messages=[message_system, message]

### Temperature by default is 0, who can set it to increase creativity

response =client.chat.completions.create(model=model, messages=messages, temperature=0)
print(response)

print("#######################################")

answer=response.choices[0].message.content
print(answer)
