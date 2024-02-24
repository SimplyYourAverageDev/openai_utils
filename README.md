# OpenAI Utility Library

This library provides a set of utility functions to interact with OpenAI's API, focusing on generating chat responses, creating text embeddings, formatting response data, and generating images from prompts. It leverages the OpenAI Python client to facilitate these tasks.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Functions](#functions)
  - [generate_chat_response](#generate_chat_response)
  - [create_text_embedding](#create_text_embedding)
  - [format_response_data](#format_response_data)
  - [generate_image_from_prompt](#generate_image_from_prompt)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Installation

To use this library, you need to have Python installed on your system. You also need to install the OpenAI Python client. You can do this by running the following command in your terminal:

```bash
pip install openai
```

## Usage

To use the functions provided by this library, you need to import the library and then call the desired function. Here's a basic example:

```python
import openai_utility_library as oai

# Generate a chat response
context = "Hello, how can I help you today?"
response = oai.generate_chat_response(context)
print(response)

# Create a text embedding
input_string = "This is a sample text."
embedding = oai.create_text_embedding(input_string)
print(embedding)

# Format response data
formatted_data = oai.format_response_data(response)
print(formatted_data)

# Generate an image from a prompt
prompt = "A beautiful sunset over the ocean."
image = oai.generate_image_from_prompt(prompt)
print(image)
```

## Functions

### generate_chat_response

This function generates a chat response based on the provided context. It supports both string and list inputs for the context.

- **Parameters:**
  - `context`: The context for the chat response. Can be a string or a list of message objects.
  - `model`: The model to use for generating the response. Default is "gpt-3.5-turbo-1106".
  - `temperature`: The temperature for the model. Default is  1.
- **Returns:** The generated chat response as a string.

### create_text_embedding

This function creates a text embedding for the given input string.

- **Parameters:**
  - `input_string`: The string for which to create the text embedding.
- **Returns:** A list representing the text embedding.

### format_response_data

This function formats the response data from OpenAI's API into a more readable format.

- **Parameters:**
  - `response`: The response object from OpenAI's API.
- **Returns:** A dictionary containing the formatted response data.

### generate_image_from_prompt

This function generates an image based on the provided prompt.

- **Parameters:**
  - `prompt`: The prompt for generating the image.
  - `quality`: The quality of the generated image. Default is 'standard'.
- **Returns:** The generated image.

## Examples

For detailed examples on how to use each function, refer to the [Usage](#usage) section.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you find any bugs or have suggestions for improvements.

## License

This library is licensed under the MIT License. See the LICENSE file for more details.