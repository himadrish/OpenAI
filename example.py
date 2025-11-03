from openai import OpenAI

client = OpenAI(api_key="Your Key")

response = client.responses.create(
    model="gpt-4o-mini",
    tools=[{"type": "web_search_preview"}],
    input="What is today's day?"
)

print(response.output_text)
