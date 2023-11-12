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
