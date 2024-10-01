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

# convert gambar menjadi array numpy
image1_np = np.array(image1)
image2_np = np.array(image2)

result = (image1_np + image2_np) * (image1_np - image2_np)

# convert hasil output
result_image = Image.fromarray(np.uint8(result))

# simpan gambar sebagai
result_image.save('hasil_operasi.png')

# tampilkan
result_image.show()
