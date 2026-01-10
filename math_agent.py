# math_agent.py
from dotenv import load_dotenv
import os
from google import genai
from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
from PIL import Image

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

math_agent = Agent(
    name="math_agent",
    model=my_model,
    instruction='''You are a math agent 
                that can answer math questions and explain the solution step by step 
                and use easy language to explain the solution.
    ''',
    description="Your internal name is math_agent",
    # tools=[Image]
)
