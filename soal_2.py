import pandas as pd

# membuat array 2 dimensi
data =[
    ["Aldi", 90,80],
    ["Jono", 50,60],
    ["Salman",65,70],
] 

# membuat DataFrame dari array 2 Dimensi
df = pd.DataFrame(data, columns=["nama", "algoritma dan struktur data 2", "matematika numerik"])

#A. Menampilkan rata-rata nilai untuk setiap mata kuliah
rata_rata_mata_kuliah = df.mean(numeric_only=True)
print("rata-rata nilai untuk setiap mata kuiah:")
print(rata_rata_mata_kuliah)

#B. Menampilkan rata-rata nilai utuk setiap mahasiswa
df['rata-rata'] =df.mean(axis=1, numeric_only=True)
print("\nRata-rata nilai untuk setiap mahasiswa:")
print(dff[['nama', 'Rata-rata']])