# english_agent.py
from dotenv import load_dotenv
import os
from google import genai
from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
from google.adk.tools.google_search_tool import GoogleSearchTool
load_dotenv()

model_id = os.getenv("MODEL")
api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    os.environ["GOOGLE_API_KEY"] = api_key
    client = genai.Client(api_key=api_key)

my_model = Gemini(
    model=model_id,  
    use_interactions_api=True      
)

english_agent = Agent(
    name="english_agent",
    model=my_model,
    instruction="You are a English agent that can answer English questions and explain the solution in easy language.",
    description="Your internal name is english_agent",
    # tools=[GoogleSearchTool()],
)
