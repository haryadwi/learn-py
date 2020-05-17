# set integer
my_set = {1, 2, 3}
print(my_set)

# set dengan menggunakan fungsi set
my_set = set([1, 2, 3])
print(my_set)

# set data campuran
my_set = {1, 2.0, "jamet", (3, 4, 5)}
print(my_set)

# tipe data set tidak bisa diisi oleh data yang sama
my_set = {1, 1, 1, 2, 2, 3, 4, 4, 5, 5, 5, 5}
print(my_set)  # output yang dihasilkan {1, 2, 3, 4, 5}

# set tidak bisa berisikan anggota list
my_set = {1, 2, [3, 4, 5]}
print(my_set)  # akan terjadi error
