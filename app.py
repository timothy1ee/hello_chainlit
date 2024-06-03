import chainlit as cl
from openai import AsyncOpenAI

endpoint_url = "https://api.runpod.ai/v2/abc/openai/v1" 

runpod_api_key = "<YOUR_RUNPOD_API_KEY>"
model = "mistralai/Mistral-7B-Instruct-v0.2"

client = AsyncOpenAI(base_url=endpoint_url, api_key=runpod_api_key)

gen_kwargs = {
    "model": model,
    "temperature": 0.7,
    "max_tokens": 500
}

@cl.on_message
async def on_message(message: cl.Message):
    message_history = cl.user_session.get("message_history", [])
    message_history.append({"role": "user", "content": message.content})

    response_message = cl.Message(content="")
    await response_message.send()

    stream = await client.chat.completions.create(messages=message_history, stream=True, **gen_kwargs)
    async for part in stream:
        if token := part.choices[0].delta.content or "":
            await response_message.stream_token(token)

    # stream = await client.completions.create(prompt=message.content, stream=True, **gen_kwargs)
    # async for part in stream:
    #     if token := part.choices[0].text or "":
    #         await response_message.stream_token(token)

    message_history.append({"role": "assistant", "content": response_message.content})
    cl.user_session.set("message_history", message_history)
    await response_message.update()

if __name__ == "__main__":
    cl.main()
