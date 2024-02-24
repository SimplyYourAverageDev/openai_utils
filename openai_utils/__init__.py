import openai

def generate_chat_response(context, model: str = "gpt-3.5-turbo-1106", temperature: float =  1) -> str:
    if isinstance(context, list):
        response = openai.chat.completions.create(
            model=model,
            messages=context,
            temperature=temperature
        )
        return response.choices[0].message.content

    elif isinstance(context, str):
        response = openai.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": context}],
            temperature=temperature
        )
        return response.choices[0].message.content

def create_text_embedding(input_string: str) -> list:
    reply = openai.embeddings.create(model="text-embedding-ada-002",
    input=input_string)
    return reply.data[0].embedding

def format_response_data(response) -> dict:
    if type(response).__name__ == 'ChatCompletion':
        simplified_data = {}
        simplified_data['text'] = response.choices[0].message.content
        simplified_data['model'] = response.model
        simplified_data['function_call'] = response.choices[0].message.function_call
        return simplified_data
    elif type(response).__name__ == 'ImagesResponse':
        simplified_data = {}
        simplified_data['ImageURL'] = response.data[0].url
        simplified_data['RevisedPrompt'] = response.data[0].revised_prompt
        return simplified_data
        

def generate_image_from_prompt(prompt: str, quality: str = 'standard'):
    image = openai.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality=quality,
        style="natural",
    )
    return image