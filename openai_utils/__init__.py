import openai

def GPT_Response(Context, model: str = "gpt-3.5-turbo-1106", temperature: float = 1) -> str:
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


def CreateEmbedding(InputString: str) -> list:
    reply = openai.Embedding.create(
        model="text-embedding-ada-002",
        input=InputString
    )
    return reply.data[0].embedding

def SimplifyResponse(Response) -> dict:
    if type(Response).__name__ == 'ChatCompletion':
        Simplified_Data = {}
        Simplified_Data['text'] = Response.choices[0].message.content
        Simplified_Data['model'] = Response.model
        Simplified_Data['function_call'] = Response.choices[0].message.function_call
        return Simplified_Data
    elif type(Response).__name__ == 'ImagesResponse':
        Simplified_Data = {}
        Simplified_Data['ImageURL'] = Response.data[0].url
        Simplified_Data['RevisedPrompt'] = Response.data[0].revised_prompt
        return Simplified_Data
        

def GenerateImage(Prompt: str, Quality: str = 'standard'):
  Image = openai.images.generate(
    model="dall-e-3",
    prompt=Prompt,
    size="1024x1024",
    quality=Quality,
    style="natural",
  )
  return Image