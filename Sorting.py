# Merge Sort 
def pengurutan_merge(data):
    if len(data) > 1:
        tengah = len(data) // 2
        bagian_kiri = data[:tengah]
        bagian_kanan = data[tengah:]

        pengurutan_merge(bagian_kiri)
        pengurutan_merge(bagian_kanan)

        i = j = k = 0

        for _ in range(len(data)):
            if i < len(bagian_kiri) and j < len(bagian_kanan):
                if bagian_kiri[i] < bagian_kanan[j]:
                    data[k] = bagian_kiri[i]
                    i += 1
                else:
                    data[k] = bagian_kanan[j]
                    j += 1
            elif i < len(bagian_kiri):
                data[k] = bagian_kiri[i]
                i += 1
            elif j < len(bagian_kanan):
                data[k] = bagian_kanan[j]
                j += 1
            k += 1


#  Quick Sort 
def pengurutan_cepat(data):
    if len(data) <= 1:
        return data
    else:
        pivot = data[0]
        lebih_kecil = []
        lebih_besar = []

        for elemen in data[1:]:
            if elemen <= pivot:
                lebih_kecil.append(elemen)
            else:
                lebih_besar.append(elemen)

        return pengurutan_cepat(lebih_kecil) + [pivot] + pengurutan_cepat(lebih_besar)


# Data 
X = [1, 5, 6, 4, 3, 3, 7, 7, 9, 0, 1, 1, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

hasil_merge = X.copy()
pengurutan_merge(hasil_merge)
print("Hasil Merge Sort:", hasil_merge)


hasil_quick = pengurutan_cepat(X)
print("Hasil Quick Sort:", hasil_quick)

##Analisis Marge Sort##
# Untuk Merge Sort, baik dalam Worst Case (Kasus Terburuk), Average Case (Kasus Rata-rata), maupun Best Case (terbaik), kompleksitas 
# waktu tetap konsisten di O(n log n). Kasus terburuk terjadi ketika data sudah terbalik, 
# tetapi algoritma ini tetap membagi dan menggabungkan data dengan cara yang efisien. 
# Dalam kasus rata-rata, proses pembagian dan penggabungan juga menghasilkan kompleksitas O(n log n), 
# dan bahkan dalam kasus terbaik, di mana data sudah terurut, Merge Sort tetap menjalankan proses pembagian. 
# Ini menunjukkan bahwa Merge Sort memiliki performa yang stabil di semua situasi.

##Analisis Quick Sort##
#Quick Sort menunjukkan karakteristik yang berbeda. Dalam kasus terburuk(Worst Case), yang biasanya terjadi ketika 
#pivot(elemen kunci) yang dipilih adalah elemen terkecil atau terbesar dalam daftar, kompleksitas waktu dapat memburuk 
#menjadi O(n²). Ini terjadi karena partisi yang sangat tidak seimbang menghasilkan banyak panggilan rekursif 
#dengan kompleksitas O(n) pada setiap langkah. Namun, dalam kasus rata-rata(Average Case ), di mana pivot biasanya membagi 
#daftar menjadi dua bagian yang lebih seimbang, Quick Sort memiliki kompleksitas O(n log n), mirip dengan Merge Sort. 
#Kasus terbaik(Best Case) juga memiliki kompleksitas O(n log n) jika pivot membagi daftar secara optimal.meskipun 
#Quick Sort dapat sangat cepat dalam praktiknya jika pivot dipilih dengan baik, ia memiliki potensi untuk melambat secara 
#signifikan dalam kondisi tertentu. Pemilihan antara kedua algoritma ini sering kali bergantung pada sifat data dan kebutuhan 
#spesifik dari aplikasi pengurutan.
