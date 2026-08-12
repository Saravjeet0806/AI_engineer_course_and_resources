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
prompt1="What is the capital of India"
prompt2="Write an essay on Social Media"
prompt3="Write about Japan in 1000 words"
prompt4="Hi"

prompts=[prompt1, prompt2, prompt3, prompt4]

for prompt in prompts:
    message={
    "role":role,
    "content":prompt
    }
    messages=[message]
    response=client.chat.completions.create(model=model, messages=messages, max_tokens=500)
    usage=response.usage
    print(f"Prompt: {prompt} -->your tokens: {usage.prompt_tokens} completion_tokens: {usage.completion_tokens} total tokens: {usage.total_tokens}  Finish Reason: {response.choices[0].finish_reason}")
    ans=response.choices[0].message.content
    print(ans)

###Prompt: Write an essay on Social Media -->your tokens: 41 completion_tokens: 500 total tokens: 541  Finish Reason: length
###Prompt: Write an essay on Social Media -->your tokens: 41 completion_tokens: 500 total tokens: 541  Finish Reason: length
###Prompt: Write about Japan in 1000 words -->your tokens: 43 completion_tokens: 500 total tokens: 543  Finish Reason: length
###Prompt: Hi -->your tokens: 36 completion_tokens: 25 total tokens: 61  Finish Reason: stop //stopped naturally whereas the above 3 prompts stopped due to max_token limit