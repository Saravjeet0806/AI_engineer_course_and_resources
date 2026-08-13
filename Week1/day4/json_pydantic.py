import os 
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key not found")

client = Groq(api_key=my_api_key)

model="llama-3.3-70b-versatile"
role="user"


##structured output

from pydantic import BaseModel
class Ticket (BaseModel):
    name:str
    email:str
    issue:str

schema=Ticket.model_json_schema()

response_format={
    "type": "json_object"
}

system_prompt=f"""
Extract the personal information form the ticket strictly based on this schema and gave a json output. {schema}
"""

message_system={
    "role":"system",
    "content": system_prompt
}

text="hello my name is Saravjeet, I have an issue with my phone. My address is 2314 New Delhi and my Email is sarav@gmail.com"

prompt=f"""
This is a customer ticket. Please extract personal information from this 
Ticket:
{text}
"""

message={
    "role":role,
    "content":prompt
}

messages = [message_system, message]

response=client.chat.completions.create(model=model, messages=messages, response_format=response_format)

ans = response.choices[0].message.content
print(ans)

import json
raw_json = ans
data_file=json.loads(raw_json)
ticket=Ticket(**data_file)

print(ticket.name)
print(ticket.email)
print(ticket.issue)