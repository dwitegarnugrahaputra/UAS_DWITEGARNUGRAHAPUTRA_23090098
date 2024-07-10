# Membuat array 2 dimensi untuk menyimpan data
data_mahasiswa = [
    ["mahasiswa 1", 90, 80],
    ["mahasiswa 2", 50, 60],
    ["mahasiswa 3", 65, 70]
]

total_algoritma = 0
total_matematika = 0

for mahasiswa in data_mahasiswa:
    total_algoritma += mahasiswa[1]
    total_matematika += mahasiswa[2]

rata_rata_algoritma = total_algoritma / len(data_mahasiswa)
rata_rata_matematika = total_matematika / len(data_mahasiswa)

print(f"rata-rata nilai algoritma dan struktur data 2: {rata_rata_algoritma}")
print(f"rata-rata nilai matematika numerik: {rata_rata_matematika}")

for mahasiswa in data_mahasiswa:
    rata_rata_mahasiswa = (mahasiswa[1] + mahasiswa[2]) / 2
    print(f"rata-rata nilai {mahasiswa[0]}: {rata_rata_mahasiswa}")
