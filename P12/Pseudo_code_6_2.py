import math

# Data masukan
datain = 'TOBEORNOTTOBEORTOBEORNOT'  # Data masukan
j = 1  # Digunakan untuk urutan kata dalam kamus dan keluaran
dictnew = [""]  # Inisialisasi kamus
W = datain[0]  # Karakter pertama
i = 0  # Indeks karakter masukan
lda = len(datain)  # Panjang data masukan
dout = []  # Inisialisasi keluaran

# Loop proses pembuatan kamus dan keluaran
while i < lda - 1:
    c = datain[i + 1]  # Karakter yang akan diproses
    Wc = W + c  # Kata W+C
    if Wc not in dictnew:  # Cek kata bila belum ada di kamus
        dictnew.append(Wc)  # Catat kata baru dalam kamus
        dout.append(W)  # Catat W sebagai keluaran
        j += 1
        W = c  # Pindahkan c ke W
    else:
        W = Wc  # Jika sudah ada di kamus, pindahkan Wc ke W
    i += 1

# Proses karakter terakhir
c = datain[i]
Wc = W + c
if Wc not in dictnew:
    dictnew.append(Wc)
    dout.append(W)

# Tampilkan keluaran dalam bentuk simbol karakter
print("Keluaran simbol karakter:", dout)

# Konversi keluaran ke dalam bentuk nilai numerik
Dout = []
for word in dout:
    if word in dictnew:
        Dout.append(255 + dictnew.index(word))
    else:
        Dout.append(ord(word))

# Tampilkan keluaran dalam bentuk numerik
print("Keluaran bentuk numerik:", Dout)

# Konversi keluaran ke dalam bentuk bitstream
Nb = math.ceil(math.log2(max(Dout)))  # Hitung panjang bit kode
bitstream = ''.join(format(num, f'0{Nb}b') for num in Dout)

# Tampilkan keluaran dalam bentuk bitstream
print("Keluaran bentuk bitstream:", bitstream)