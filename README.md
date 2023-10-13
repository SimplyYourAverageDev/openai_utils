# OpenAI Utilities README

## Package Name: openai-utilities

When imported, the package is referred to as `openai_utils`.

## Installation

To install the package, run:

```
pip install openai-utilities
```

## Overview

This Python package provides utility functions for interacting with OpenAI's GPT-3.5-turbo and GPT-4 models to generate text completions and embeddings. It simplifies the process of generating text completions and embeddings.

## Dependencies

- `openai`
- `numpy`

## Importing

After installation, import the package using:

```python
import openai_utils
```

## Functions

### AskGPT

#### Description

Generates text completions using OpenAI's GPT-3.5-turbo or GPT-4 models.

#### Parameters

- `model`: The GPT model to use for text generation. Available options: "gpt-3.5-turbo", "gpt-4".
- `Context`: Can be either a string or a list of message objects.
  - If a string, it serves as the prompt for the text completion.
  - If a list, it should contain message objects in the format `{"role": "user/system", "content": "message content"}`.
- `temperature`: Controls the randomness of the output (default is 1).

#### Returns

Returns a string containing the generated text.

#### Example

```python
response = openai_utils.AskGPT(model="gpt-4", Context="How are you?", temperature=0.7)
```

### CreateEmbedding

#### Description

Generates text embeddings for a given string using OpenAI's text-embedding models.

#### Parameters

- `String`: The input string for which the embedding will be generated.

#### Returns

Returns a list representing the generated text embedding.

#### Example

```python
embedding = openai_utils.CreateEmbedding(String="Hello, world!")
```

## Usage

First, ensure you have the `openai` and `numpy` packages installed. Then import the `openai_utils` package and use the functions as demonstrated in the examples above.

## License

MIT License