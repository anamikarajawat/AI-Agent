from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
import os


model_id = os.getenv("MODEL")

my_model = Gemini(
    model=model_id,
    use_interactions_api=True,
    thinking_budget=0 
)

def create_router_agent(sub_agents):
    model = my_model
    
    return Agent(
        name="Router_Agent",
        model=model,
        instruction="""
            You are a ROUTER agent.

            ONLY decide which agent should handle the user's message.
            DO NOT answer, greet, explain, or generate normal text.

            ### ROUTING RULES
            - If message contains greeting words (hi, hello, hey) → greeting_agent
            - If message contains math keywords (LCM, HCF, equation, calculate) → math_agent
            - If message contains history keywords (history, dynasty, empire, ancient, medieval, modern, Indian) → history_agent
            - If message contains English keywords (grammar, meaning, sentence) → english_agent
            - Otherwise → transfer to fallback_agent (or ignore if none)
            - If message contains history keywords (history, Indian, dynasty, empire, ancient, medieval, modern) → history_agent
            - If message contains math keywords (LCM, HCF, equation, calculate, sum, product, solve) → math_agent
            - If message contains English keywords (grammar, meaning, sentence, word, vocabulary) → english_agent
    
            ### IMPORTANT
            - CALL `transfer_to_agent` for routing
        """,
        sub_agents=sub_agents
    )



# def create_router_agent(sub_agents):
    # Router uses a capable model to decide routing
    # model = my_model
    
    # return Agent(
    #     name="Router_Agent",
    #     model=model,
    #     instruction="""
    #         You are a ROUTER agent.

    #         Your ONLY responsibility is to decide which agent should handle the user's message.

    #         ### STRICT RULES (MANDATORY)
    #         1. DO NOT answer user questions.
    #         2. DO NOT greet the user.
    #         3. DO NOT explain your decision.
    #         4. DO NOT repeat or summarize user input.
    #         5. DO NOT generate any normal text.

    #         ### ROUTING RULES
    #         - If the message is a greeting or casual talk → transfer to greeting_agent
    #         - If the message is about math → transfer to math_agent
    #         - If the message is about history → transfer to history_agent
    #         - If the message is about English → transfer to english_agent
    #         - If unsure → transfer to greeting_agent
    #         - If message contains greeting words → greeting_agent
    #         - If message contains math keywords (LCM, HCF, equation, calculate) → math_agent
    #         - If message contains history keywords (history, dynasty, empire, ancient, medieval, modern) → history_agent
    #         - If message contains English keywords (grammar, meaning, sentence) → english_agent
    #         - If unsure → fallback to greeting_agent


    #         ### IMPORTANT
    #         - When transferring, CALL `transfer_to_agent`
    #         - When transferring, generate NOTHING except the function call
    #         - Never call `transfer_to_agent` and also speak
    #     """,
    #     sub_agents=sub_agents
    # )