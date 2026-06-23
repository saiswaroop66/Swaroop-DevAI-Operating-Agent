import requests
from urllib.parse import quote

def generate_image(prompt):

    image_url = f"https://image.pollinations.ai/prompt/{quote(prompt)}"

    image_path = "generated_image.png"

    response = requests.get(image_url)

    if response.status_code == 200:
        with open(image_path, "wb") as f:
            f.write(response.content)

        return image_path

    return "Image generation failed"
