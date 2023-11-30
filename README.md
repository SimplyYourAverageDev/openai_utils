# openai-utilities Library Documentation

## Overview

The `openai-utilities` library is a Python package that provides easy-to-use functions to interact with OpenAI's GPT and DALL-E models. This library simplifies the process of generating text responses, embeddings, and images using OpenAI's API.

## Installation

To install the `openai-utilities` library, run the following command:

```bash
pip install openai-utilities
```

## Importing the Library

After installation, you can import the library using:

```python
import openai-utils
```

## Features and Usage

### 1. AskGPT

#### Description

Generates a text response using the specified GPT model.

#### Usage

```python
import openai
import openai_utils as OA
openai.api_key = "sk-????"

OA.AskGPT(model: str, Context, temperature: float = 1) -> str
```

- `model`: The identifier of the GPT model to be used.
- `Context`: The context or prompt to be provided to the model. Can be a string or a list of message objects.
- `temperature`: Controls the randomness of the response. Higher values generate more random responses.

### 2. CreateEmbedding

#### Description

Generates an embedding for a given string using OpenAI's embedding model.

#### Usage

```python
import openai
import openai_utils as OA
openai.api_key = "sk-????"

OA.CreateEmbedding(String: str) -> list
```

- `String`: The text string for which the embedding is to be generated.

### 3. ParseResponse

#### Description

Parses the response from the GPT model and extracts useful information.

#### Usage

```python
import openai
import openai_utils as OA
openai.api_key = "sk-????"

message = [] # Your Messages

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=message,
)

OA.ParseResponse(completion)
```

- `Response`: The response object received from the GPT model.

### 4. GenerateImage

#### Description

Generates an image based on a provided prompt using the DALL-E model.

#### Usage

```python
import openai_utils as OA
import openai
openai.api_key = "sk-????"

OA.GenerateImage(Prompt: str)
```

- `Prompt`: The text prompt based on which the image will be generated.

## Requirements

- Python 3.x
- OpenAI API key set as an environment variable or within the code.

## Examples

### Example 1: Generating Text Response

```python
response = AskGPT("gpt-3.5-turbo", "What is the capital of France?")
print(response)
```

### Example 2: Creating an Embedding

```python
import openai
import openai_utils as OA
openai.api_key = "sk-????"

OA.embedding = CreateEmbedding("Hello, world!")
print(embedding)
```

### Example 3: Parsing a GPT Response

```python
import openai
import openai_utils as OA
openai.api_key = "sk-????"

message = [] # Your example messages

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=message,
)

parsed_response = ParseResponse(completion)
print(parsed_response)
```

### Example 4: Generating an Image

```python
import openai
import openai_utils as OA

openai.api_key = "sk-????"
OA.GenerateImage("A sunset over a mountain range")
```

## Additional Notes

- Ensure that you have a valid OpenAI API key.
- The library is designed to be simple and intuitive, making it easy to integrate OpenAI's powerful models into your applications.