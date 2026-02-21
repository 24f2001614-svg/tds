from PIL import Image
import os
img = Image.open("opt.webp")
img = img.convert("P", palette=Image.ADAPTIVE, colors=256)
img.save("compressed.webp", "WEBP", lossless=True, quality=100, method=6)
print(f"Compressed size: {os.path.getsize('compressed.webp')} bytes")
