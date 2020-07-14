try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

# Load sample image
image=Image.open("resources/sample.png")

config="-c tessedit_char_whitelist=0123456789."
image_as_str = pytesseract.image_to_string(image, config=config)
print(image_as_str)
