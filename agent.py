import os
import asyncio
from dotenv import load_dotenv
from google import genai
from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
from .math_agent import math_agent
from .history_agent import history_agent
from .english_agent import english_agent
from .router_agent import create_router_agent
import json

# Monkey-patch json to handle bytes serialization errors in ADK telemetry
_original_default = json.JSONEncoder.default

def _new_default(self, o):
    if isinstance(o, bytes):
        return f"<bytes len={len(o)}>"
    return _original_default(self, o)

json.JSONEncoder.default = _new_default

# Load environment variables
load_dotenv()
model_id = os.getenv("MODEL")
# Setup API Key globally for the module
api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    os.environ["GOOGLE_API_KEY"] = api_key
    # Configure genai if needed for direct usage, though ADK handles it too
    # genai.configure(api_key=api_key)
    client = genai.Client(api_key=api_key)

my_model = Gemini(
    model=model_id,
    use_interactions_api=True,
    thinking_budget=0 
)

# Initialize the Greeting Agent (formerly root)
greeting_agent = Agent(
    name="greeting_agent",
    model=my_model,
    # instruction='''
    #     You are a friendly, helpful educational assistant for students grades 1-12.

    #     ## RESPONSE RULES (MANDATORY):
    #     1. **Always conversational** - Use "Hi!", "Great question!", "Let me explain"
    #     2. **Short paragraphs** - 2-3 sentences max per paragraph
    #     3. **Bullet points** for lists/steps
    #     4. **Bold key terms**: **photosynthesis**, **Pythagoras theorem**
    #     5. **Grade-appropriate**: Simple words for younger students
    #     6. **Encourage questions**: End with "What else would you like to know?"

    #     ## FORMATTING:
    #     - **Headers**: ## Main Idea
    #     - **Bullets**: - Item 1
    #     - **Numbers**: 1. Step one
    #     - **No walls of text**
    # ''',
    instruction="""
        You are a helpful assistant. 
        1. Greet the user only ONCE at the start of a new session.
        2. Do NOT ask for name repeatedly.
        3. Do NOT greet the user again after the first greeting.
        4. genrated response should be easy to understand and implement. and show it in new line if paragraph is there make it readable.
        6. If the questions about math, history, english call router_agent.
        7. Answer questions other then math and history and english questions.
        8. Use google search tool to answer questions.
    """,
    description="Assistant for greetings and solutions",
    # tools=[
    #     google_search
    #    GoogleSearchTool(bypass_multi_tools_limit=True)
    #     ], 
    # sub_agents=[] # No sub-agents for the leaf node
)

# Initialize the Router as the new Root Agent
# This is what ADK will load as the entry point
root_agent = create_router_agent(sub_agents=[greeting_agent, math_agent, history_agent, english_agent])
# response = root_agent.run("Latest updates on Python 3.12")
# print(response)

# root_agent = Agent(
#     name="greeting_Agent",
#     model=Gemini(model="models/gemini-2.5-flash-lite-lite"), 
#     instruction=" You are a helpful assistant that Ask for the user's name and greet them by name, generates creative solutions to the user's problem. And the solution should be easy to understand and implement. ",
#     description="Your internal name is greeting_Agent",
# )
print(f"DEBUG: Loaded Agent with model: {root_agent.model}")