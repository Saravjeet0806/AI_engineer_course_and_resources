import os 
from pathlib import Path
from time import sleep
from dotenv import load_dotenv
from groq import Groq
import re 

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("Api key not found")

client = Groq(api_key=my_api_key)
model = "qwen/qwen3.6-27b" # Note: Ensure you use a valid Groq model identifier

def get_product_price(product):
    if product == "iPhone 17":
        return 100000
    elif product == "iPhone 16":
        return 80000
    else:
        return 0

def calculator(expression):
    try:
        return eval(expression)
    except:
        return "calculation error!"        

tools = {
    "get_product_price" : get_product_price,
    "calculator": calculator
}

system_prompt = """
You are a shopping assistant.

You have these tools:
get_product_price(product)
calculator(expression)

IMPORTANT: 
call the tools exactly like these examples:

Action: get_product_price("iPhone 17")
Action: calculator("20000-10000")

Never write:
calculator(expression="20000-10000")
Follow these rules:

1. Decide what you need to do next.
2. Call only one tool at a time.
3. After writing an Action, stop immediately.
4. Never guess or invent a tool result.
5. Wait until you receive an Observation.
6. Then decide your next action.
7. When the task is complete, give the final answer.

Format : 

Thought: what you need to do
Action: tool_name(argument)

When finished:

Final Answer : your answer
"""

def run_agent(question):
    # FIX 1: Renamed from 'message' to 'messages' to match the loop references
    messages = [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": question
        }
    ]

    for step in range(5):
        print("\n------------------")
        print("STEP", step+1)
        print("--------------------")

        response = client.chat.completions.create(model=model, messages=messages, temperature=0, max_tokens=200)

        answer = response.choices[0].message.content

        print(answer)

        # agent has finished
        if "Final Answer:" in answer:
            break

        # find the action
        match = re.search(
            r"Action:\s*(\w+)\((.*?)\)",
            answer
        )

        if match:
            tool_name = match.group(1)
            tool_input = match.group(2)
            tool_input = tool_input.strip()
      
            tool_input = tool_input.strip('"')

            # run the tool
            if tool_name in tools:
                tool = tools[tool_name]
                observation = tool(tool_input) 
            else:
                observation = "Tool not found"    

            print("Observation: ", observation)

            # add LLM response to memory
            messages.append({
                "role": "assistant",
                "content": answer
            })    

            messages.append({
                "role": "user",
                "content": "Observation: " + str(observation)
            })

            sleep(5)

prompt = """
I have 500000 rupees. What is the price of an iphone 17?
and how much money will I have left?
"""
run_agent(prompt)