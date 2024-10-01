from PIL import Image
import numpy as np
import requests
from io import BytesIO

url1 = "https://images6.alphacoders.com/135/thumb-1920-1353817.jpg"
response1 = requests.get(url1)
image1 = Image.open(BytesIO(response1.content))

url2 = "https://images3.alphacoders.com/135/1353818.jpg"
response2 = requests.get(url2)
image2 = Image.open(BytesIO(response2.content))

image2 = image2.resize(image1.size)

image1_np = np.array(image1)
image2_np = np.array(image2)

if image1_np.ndim == 3:  # Convert to grayscale if RGB
    image1_np = np.mean(image1_np, axis=2).astype(np.uint8)
if image2_np.ndim == 3:  # Convert to grayscale if RGB
    image2_np = np.mean(image2_np, axis=2).astype(np.uint8)

# 1. (P and Q) + (P nand Q)
and_result = np.bitwise_and(image1_np, image2_np)
nand_result = np.invert(and_result)
result_1 = np.bitwise_or(and_result, nand_result)

# 2. (P or Q) + (P nor Q)
or_result = np.bitwise_or(image1_np, image2_np)
nor_result = np.invert(or_result)
result_2 = np.bitwise_or(or_result, nor_result)

result_image_1 = Image.fromarray(result_1)
result_image_2 = Image.fromarray(result_2)

result_image_1.save('hasil_operasi_1.png')
result_image_2.save('hasil_operasi_2.png')

result_image_1.show()
result_image_2.show()
