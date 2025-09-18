from PIL import Image

webp_image = Image.open("SCRIPTS\Logo1.webp")

webp_image.save("Logo1.png", "PNG")

print("Conversion complete.")
