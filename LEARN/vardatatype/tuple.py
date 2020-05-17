white = (255, 255, 255)
red = (255, 0, 0)

print(white)
print(red[1])
print(red[0])

# mencoba mengubah tuple indeks ke 0 menjadi 128
red[0] = 128  # ini akan menghasilkan error karena sifart tipe data tuple tidak dapat diubah seperti list
