from PIL import Image
import numpy as np

image = Image.open("sample.jpg")
img_array = np.array(image)

print("Shape:", img_array.shape)
print("Pixel [0][0]:", img_array[0][0])

if len(img_array.shape) == 3:
    print("Channels: RGB")
else:
    print("Grayscale")

print("\nExplanation: Images are matrices of pixel values (0-255).")
