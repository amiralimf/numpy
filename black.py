import numpy as np
from PIL import Image

image_path = "berserk.png"
output_path = "berserk_gray.png"

original_image = Image.open(image_path)
image_data = np.asarray(original_image)

print(image_data.shape)

weight = [0.2126, 0.7152, 0.0722]
grayscale = image_data @ weight
grayscale = grayscale.astype('uint8')

grayscale_imgage = Image.fromarray(grayscale)
grayscale_imgage.save(output_path)