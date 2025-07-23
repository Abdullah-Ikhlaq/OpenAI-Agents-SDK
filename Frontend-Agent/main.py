from agents import Runner, Agent, OpenAIChatCompletionsModel, AsyncOpenAI, RunConfig
from openai.types.responses import ResponseTextDeltaEvent #For Raw Responses

import os
from dotenv import load_dotenv
import chainlit as cl


load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True # Because we are not using Open Ai API key
    
)

agent = Agent(
    name="Frontend Expert",
    instructions="You are a frontend expert",
)


# Chat History Decorator

@cl.on_chat_start
async def handle_start():
    cl.user_session.set("history", [])
    await cl.Message(content="Hello! I am a Front end agent. How can I help you today?").send()


# Message Decorator

@cl.on_message
async def handle_message(message : cl.Message):

# For User History

    history = cl.user_session.get("history")

    history.append({ "role": "user", "content": message.content })

  # For Streaming 
    msg = cl.Message(content="|")
    await msg.send()


    result = Runner.run_streamed(    # No need of await now
        agent,
        input=history,
        run_config=config 
    )

    # For Streaming 
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            await  msg.stream_token(event.data.delta)


# For Agent History
    history.append({ "role": "assistant", "content": result.final_output})
    cl.user_session.set("history", history)
    # await cl.Message(content=result.final_output).send()