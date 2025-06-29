from PIL import Image
import os
os.makedirs("images", exist_ok=True)
img = Image.new("RGB", (200, 200), (255, 255, 255))
img.save("images/in.png", "PNG")
print("✅ Created images/in.png")
