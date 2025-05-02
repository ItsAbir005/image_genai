from google import genai
from google.genai import types
import os
import platform
import subprocess

api_key = os.environ.get("GOOGLE_API_KEY")
client = genai.Client(api_key=api_key)

prompt = "bengali brainrot cartoon, 4k, 8k, trending on artstation, highly detailed, cinematic lighting, hyper realistic, award winning photography, masterpiece, best quality, 1girl, solo, looking at viewer, cute face, short hair, blue hair, bangs, hair between eyes, open mouth, white background"

response = client.models.generate_content(
    model="gemini-2.0-flash-exp-image-generation",
    contents=prompt,
    config=types.GenerateContentConfig(response_modalities=["Text", "Image"])
)

for i, part in enumerate(response.candidates[0].content.parts):
    if hasattr(part, 'inline_data') and part.inline_data is not None:
        mime_type = part.inline_data.mime_type
        extension = mime_type.split('/')[-1] if mime_type else "bin"
        filename = f"cartoon_image.{extension}"
        
        with open(filename, "wb") as f:
            f.write(part.inline_data.data)
        
        system = platform.system()
        if system == "Windows":
            os.startfile(filename)
        elif system == "Darwin":
            subprocess.call(["open", filename])
        else:
            subprocess.call(["xdg-open", filename])



