import asyncio

from agents import Agent, Runner

URL = "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi6ddk9aoWCubUr45ozFnUp3prIda9Dz7gq_THlYj-_aRVUDvDfF587FSj2jbyfjYUoW20sbVYk1D1yjayfLastXb2xlzf2d_GIDt9RucQWbXvnYsJ4d5kvKeQh6zRkRG6A_KAwi79Jh-aqooSULA9IGrXhdjY1inc7RcOXkXcS8sXWUXNXJ3VUxHA4J1o/w1684-h1069-p-k-no-nu/HL.jpeg"


async def main():
    agent = Agent(
        name="Assistant",
        instructions="You are a helpful assistant.",
    )

    result = await Runner.run(
        agent,
        [
            {
                "role": "user",
                "content": [{"type": "input_image", "detail": "auto", "image_url": URL}],
            },
            {
                "role": "user",
                "content": "What do you see in this image?",
            },
        ],
    )
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())