# workon ocr

# From Pillow
from PIL import Image
# Requires Tesseract to be installed (avail via Brew)
import pytesseract

# Set path for image
path='/path/to/image/image.jpg'
# Crack open image
im=Image.open(path)
# Convert to string
tess=pytesseract.image_to_string(im)
# Print it out
print(tess)

# Could be written shorter like this:
# print(pytesseract.image_to_string(Image.open('/path/to/image.jpg')))