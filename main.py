from langchain_openai import ChatOpenAI
from langchain_together import ChatTogether
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts.chat import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import Runnable
from langchain_core.runnables import RunnableConfig
from typing import cast
from dotenv import load_dotenv

import chainlit as cl
import os

load_dotenv()

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

@cl.on_chat_start # decorator
async def on_chat_start():
    # Default usage of TogetherAI
    """
    model = ChatOpenAI(
        base_url="https://api.together.xyz/v1",
        api_key=os.environ["KEY_TOGETHERAI"],
        model="mistralai/Mixtral-8x7B-Instruct-v0.1",
        streaming=True,)
    """
    model = ChatMistralAI(
        model="open-mixtral-8x22b",
        temperature=1,
        streaming=True,)
    
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You're a friendly chatbot. Be funny and easy to chat with about general topics in life. Joke around when you don't have an answer to the question. Use Traditional Chinese only.",
            ),
            ("human", "{question}"),
        ]
    )
    runnable = prompt | model | StrOutputParser() # prompt -> model -> StrOutputParser()
    """
    def StrOutputParser(x):
        return(x['content'])
    """
    cl.user_session.set("runnable", runnable)

"""
System: <system prompt>
Human: <human prompt1>
Assistant: <assistant prompt1>
Human: <human prompt2>
Assistant: <assistant prompt2>
Human: <human prompt3>
Assistant: <assistant prompt3>


"""

@cl.on_message
async def on_message(message: cl.Message):
    # runnable = cast(Runnable, cl.user_session.get("runnable"))  # type: Runnable
    runnable = cl.user_session.get("runnable")

    msg = cl.Message(content="")
    # runnable.invoke({"question": message.content})

    async for chunk in runnable.astream(
        {"question": message.content},
        config=RunnableConfig(callbacks=[cl.LangchainCallbackHandler()]),
    ):
        await msg.stream_token(chunk)

    await msg.send()
