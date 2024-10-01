from PIL import Image
import numpy as np
import requests
from io import BytesIO

# download image1 from URL
url1 = "https://images6.alphacoders.com/135/thumb-1920-1353817.jpg"
response1 = requests.get(url1)
image1 = Image.open(BytesIO(response1.content))

# download image2 from URL
url2 = "https://images3.alphacoders.com/135/1353818.jpg"
response2 = requests.get(url2)
image2 = Image.open(BytesIO(response2.content))

# to resize image2 to match image1's size
image2 = image2.resize(image1.size)

# convert images to numpy arrays
image1_np = np.array(image1)
image2_np = np.array(image2)

# perform the operation
result = (image1_np + image2_np) * (image1_np - image2_np)

# convert the result back to an image
result_image = Image.fromarray(np.uint8(result))

# save the resulting image
result_image.save('hasil_operasi.png')

# show the result image
result_image.show()
