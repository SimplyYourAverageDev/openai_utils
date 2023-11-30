import openai

def AskGPT(model: str, Context, temperature: float = 1) -> str:
    if type(Context) == list:

        response = openai.chat.completions.create(
            model=model,
            messages=Context,
            temperature=temperature
        )
        return response.choices[0].message.content

    elif type(Context) == str:

        response = openai.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": Context}],
            temperature=temperature
        )
        return response.choices[0].message.content


def CreateEmbedding(String: str) -> list:
    reply = openai.Embedding.create(
        model="text-embedding-ada-002",
        input=String
    )
    return reply.data[0].embedding

def ParseResponse(Response):
    MainParse = {}
    MainParse['text'] = Response.choices[0].message.content
    MainParse['model'] = Response.model
    MainParse['function_call'] = Response.choices[0].message.function_call
    return MainParse

def GenerateImage(Prompt: str):
  openai.images.generate(
    model="dall-e-3",
    prompt=Prompt,
    size="1024x1024",
    quality="standard",
    style="natural",
  )