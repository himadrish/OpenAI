from openai import OpenAI

client = OpenAI(api_key="Your Key")

response = client.responses.create(
    model="gpt-4o-mini",
    tools=[{"type": "web_search_preview"}],
    input="What was a President Trump news story from today?"
)

print(response.output_text)
