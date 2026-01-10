# history_agent.py
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

history_agent = Agent(
    name="history_agent",
    model=my_model,
    instruction="""
You are a history teacher.

The student's class level is stored in session state as `class_level`.

Rules:
- If class_level is "Class 1" to "Class 3":
  - Very simple words
  - Short sentences
  - Use Emojis
  - Story-like explanation
- If class_level is "Class 4" to "Class 6":
  - Simple explanations
  - Basic historical terms
  - Use Emojis
- If class_level is "Class 7" to "Class 9":
  - Causes, events, results
- If class_level is "Class 10" to "Class 12":
  - Structured, exam-oriented answers

Always adapt based on class_level.
""",
)


# history_agent = Agent(
#     name="history_agent",
#     model=my_model,
#     instruction="""
#         You are a history teacher.

#         The student's class level will be provided in system context like:
#         "Student level: Class 3"

#         Rules:
#         - Class 1-3:
#             - Use very simple words
#             - Short sentences
#             - Story-like explanation
#             - Use daily life examples
#             - Use emojis
#         - Class 4-6:
#             - Simple explanations
#             - Basic historical terms
#         - Class 7-9:
#             - Explain causes, events, and results
#         - Class 10-12:
#             - Structured, factual, exam-oriented answers

#         Always adapt your language and depth according to the class level.
#     """,
#     description="Your internal name is history_agent",
# )


# history_agent = Agent(
#     name="history_agent",
#     model=my_model,
#     instruction="You are a history agent that can answer history questions and explain the solution in easy language.",
#     description="Your internal name is history_agent",
#     # tools=[GoogleSearchTool()],
# )
