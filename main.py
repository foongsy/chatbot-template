from langchain_openai import ChatOpenAI
from langchain_core.prompts.chat import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import Runnable
from langchain_core.runnables.config import RunnableConfig

import chainlit as cl
import os

"""
# Uncomment this code block and add follow variables to enable descope authentication
# Reference: https://docs.chainlit.io/authentication/oauth#descope
# OAUTH_DESCOPE_CLIENT_ID
# OAUTH_DESCOPE_CLIENT_SECRET
# CHAINLIT_AUTH_SECRET <-- run `chainlit create-secret` for a new secret value 

@cl.oauth_callback
def oauth_callback(
  provider_id: str,
  token: str,
  raw_user_data: Dict[str, str],
  default_user: cl.User,
) -> Optional[cl.User]:
  return default_user
"""

@cl.on_chat_start
async def on_chat_start():
    # Default usage of TogetherAI
    model = ChatOpenAI(
        base_url="https://api.together.xyz/v1",
        api_key=os.environ["KEY_TOGETHERAI"],
        model="mistralai/Mixtral-8x7B-Instruct-v0.1",
        streaming=True,)
    
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You're a friendly chatbot who speaks in Traditional Chinese only. Be funny and easy to chat with about general topics in life. Joke around when you don't have an answer to the question.",
            ),
            ("human", "{question}"),
        ]
    )
    runnable = prompt | model | StrOutputParser()
    cl.user_session.set("runnable", runnable)


@cl.on_message
async def on_message(message: cl.Message):
    runnable = cl.user_session.get("runnable")  # type: Runnable

    msg = cl.Message(content="")

    async for chunk in runnable.astream(
        {"question": message.content},
        config=RunnableConfig(callbacks=[cl.LangchainCallbackHandler()]),
    ):
        await msg.stream_token(chunk)

    await msg.send()
