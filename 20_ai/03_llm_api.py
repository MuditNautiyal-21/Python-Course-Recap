'''
Since we cannot manage to have one of the best (parameter-wise) models in the world on our own hardware, we will use the OpenAI API to access the GPT model.
'''

key = "Insert_your_API_key_here"

from openai import OpenAI
client = OpenAI(api_key=key)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "What is the capital of France?"
        }
    ]
)
print(response.choices[0].message.content)
# Note: The API key should be kept secret and not hard-coded in production code.
# The above code is a simple example of how to use the OpenAI API to get a response from the GPT model.
# Make sure to install the OpenAI Python package with `pip install openai`
# and replace the API key with your own key from OpenAI.

# For now, this won't work, since the quota is expired but you can always recharge your own api key at https://platform.openai.com/account/api-keys and use it in the code above.