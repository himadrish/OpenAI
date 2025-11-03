from openai import OpenAI
import base64
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()


def encode_image(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")
    
base64_image1 = encode_image("Picture.png")
base64_image2 = encode_image("test.jpg")

response = client.responses.create(
    model="gpt-4.1",
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "Add two Pictures side by side having ocean in background."},
                {
                    "type": "input_image",
                    "image_url": f"data:image/jpeg;base64,{base64_image1}",
                },
                {
                    "type": "input_image",
                    "image_url": f"data:image/jpeg;base64,{base64_image2}",
                },
            ],
        }
    ],
    tools=[{"type": "image_generation", "input_fidelity": "high", "partial_images": 0}],
)

# Extract the edited image
image_data = [
    output.result
    for output in response.output
    if output.type == "image_generation_call"
]

if image_data:
    image_base64 = image_data[0]
    with open("woman_with_logo.png", "wb") as f:
        f.write(base64.b64decode(image_base64))