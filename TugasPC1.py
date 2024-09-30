from PIL import Image
import numpy as np

# cari dari file komputer
image1 = Image.open(r"C:\Users\Kiraitsu\Downloads\__sparkle_and_sparkle_honkai_and_1_more_drawn_by_butyou_mika1412__8bfffa81080e79dc8d66cae48d6e92b7.jpg")
image2 = Image.open(r"C:\Users\Kiraitsu\Downloads\__sparkle_honkai_and_1_more_drawn_by_torriet__ea8665acacab05a9349fc2d5d8934705.jpg")

# untuk mengubah ukuran gambar dua agar sesuai dengan gambar satu
image2 = image2.resize(image1.size)

# mengubah gambar menjadi array numpy
image1_np = np.array(image1)
image2_np = np.array(image2)

result = (image1_np + image2_np) * (image1_np - image2_np)

# mengubah kembali hasil operasi menjadi gambar
result_image = Image.fromarray(np.uint8(result))

# menyimpan hasil gambar
result_image.save('hasil_operasi.png')

# menampilkan hasil gambar
result_image.show()
