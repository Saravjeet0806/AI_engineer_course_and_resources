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

def llm_ans(prompt):
    message={
        "role" : "user",
        "content": prompt
    }
    messages=[message]
    response=client.chat.completions.create(model=model, messages=messages)
    ans=response.choices[0].message.content
    return ans

# bad_prompt="""
# This is a user complaint:
# My phone is not working
# Classify this 
# """

# print(llm_ans(bad_prompt))

good_prompt="""
#ROLE:
You are a support assistant at a mobile/laptop company
#TASK
You have to classify the issue in a category
#CONSTRAINT
You have to classify the issue in one of the three categories i.e billing, technical, return.
#OUTPUT FORMAT
Your answer should be one work only. The one word should be one of the categories give in the contraints
#EXAMPLE
For eg. if a user complains about a refund then the category is Return
#FALLBACK
If the issue is unrelated to all the categories mentioned in contraints, then the answer should be Other 
This is a user complaint:
My ps5 is not working
""" 

print(llm_ans(good_prompt))