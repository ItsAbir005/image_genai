from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import base64
import os
import binascii
api_key = os.environ.get("GOOGLE_API_KEY")
client = genai.Client(api_key=api_key)

prompt = (
    "i want you generate any beutiful image from your imagination in cartoon style "
)

response = client.models.generate_content(
    model="gemini-2.0-flash-exp-image-generation",
    contents=prompt,
    config=types.GenerateContentConfig(response_modalities=["Text", "Image"])
)

image_saved = False
for i, part in enumerate(response.candidates[0].content.parts):
    if part.inline_data:
        mime_type = part.inline_data.mime_type or "application/octet-stream"
        try:
            image_data = base64.b64decode(part.inline_data.data)
            image = Image.open(BytesIO(image_data))
            extension = mime_type.split('/')[-1]
            filename = f"tech_innovators_logo.{extension}"

            image.save(filename)
            image.show()
            image_saved = True

        except Exception as img_error:
            debug_file = "image_data.base64.txt"
            b64_str = (
                part.inline_data.data
                if isinstance(part.inline_data.data, str)
                else base64.b64encode(part.inline_data.data).decode("utf-8")
            )
            with open(debug_file, "w") as f:
                f.write(b64_str)



