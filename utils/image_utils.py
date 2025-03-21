import base64
from io import BytesIO
from PIL import Image, ImageDraw

def generate_test_image(text: str = "GA Output") -> str:
    # Create a simple image using Pillow
    img = Image.new("RGB", (300, 100), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.text((10, 40), text, fill=(0, 0, 0))

    # Save image to a buffer
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    # Encode as base64 and return as data URI
    base64_str = base64.b64encode(buffer.read()).decode("utf-8")
    return f"data:image/png;base64,{base64_str}"
