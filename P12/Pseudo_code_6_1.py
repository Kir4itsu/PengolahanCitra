import collections
import heapq

# Input data
Dinput = 'this is an example of a huffman tree'  # data masukan
L = len(Dinput)  # hitung panjang data

# Inisialisasi vektor konversi data masukan dan histogram
DinputNum = [ord(char) for char in Dinput]  # konversi karakter ke ASCII
Hist = [0] * 256  # inisialisasi histogram untuk 256 karakter ASCII

# Loop konversi ASCII data masukan dan histogram
for num in DinputNum:
    Hist[num] += 1

# Hitung probabilitas
PHist = [count / L for count in Hist]

# Urutkan probabilitas besar ke kecil
sorted_indices = sorted(range(256), key=lambda x: PHist[x], reverse=True)
PHist_sorted = [PHist[i] for i in sorted_indices if PHist[i] > 0]
symbols_sorted = [i for i in sorted_indices if PHist[i] > 0]

# Huffman tree creation
heap = [[weight, [symbol, ""]] for symbol, weight in zip(symbols_sorted, PHist_sorted)]
heapq.heapify(heap)

while len(heap) > 1:
    low = heapq.heappop(heap)
    high = heapq.heappop(heap)
    for pair in low[1:]:
        pair[1] = '0' + pair[1]
    for pair in high[1:]:
        pair[1] = '1' + pair[1]
    heapq.heappush(heap, [low[0] + high[0]] + low[1:] + high[1:])

# Create Huffman dictionary
huff_dict = {symbol: code for _, [symbol, code] in enumerate(heapq.heappop(heap)[1:])}

# Encoding input
hcode = ''.join(huff_dict[num] for num in DinputNum)

# Decoding bit stream
reverse_huff_dict = {v: k for k, v in huff_dict.items()}
dhsig = []
code = ""
for bit in hcode:
    code += bit
    if code in reverse_huff_dict:
        dhsig.append(reverse_huff_dict[code])
        code = ""

# Konversi ASCII ke karakter
Drec = ''.join(chr(num) for num in dhsig)

# Output hasil
print("Original Input: ", Dinput)
print("Encoded Data: ", hcode)
print("Decoded Data: ", Drec)