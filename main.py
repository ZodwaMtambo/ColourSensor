import numpy as np
from PIL import Image

image = Image.open ("images/20221225_174227.jpg")

image_array = np.array(image)

print("shape", image_array.shape)
print("Top-left pixel:", image_array[0,0])
print("Center pixel:", image_array[1500,2000])
print("Top-right:", image_array[0, 3999])
print("Bottom-left:", image_array[2999, 0])
print("Bottom-right:", image_array[2999, 3999])
print("Array shape:", image_array.shape)
print("Data type:", image_array.dtype)