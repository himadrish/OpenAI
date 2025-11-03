from PIL import Image
import pillow_heif  # pip install pillow-heif

# Open HEIC image
heif_file = pillow_heif.open_heif("Picture3.png")
img = Image.frombytes(
    heif_file.mode, 
    heif_file.size, 
    heif_file.data,
    "raw"
)

# Save as PNG or JPEG
img.save("Picture5.png", format="PNG")
