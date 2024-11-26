<h1>Jessica Andryani</h1>
F55123051
Informatika B

<h3>Analisis Kuis Kedua</h3>
<h4>Naise Bayes</h4>
    Program ini sangat unik dan menarik. Pertama, ia menghasilkan 50 angka acak yang unik dari 1 sampai 100, dengan menggunakan seed agar hasilnya konsisten setiap kali dijalankan. Setelah itu, angka-angka ini diberi label, di mana angka genap diberi label 1 dan angka ganjil diberi label 0. Ini adalah langkah awal yang bisa kita gunakan jika kita ingin membangun model klasifikasi, seperti “Naive Bayes”, meskipun program ini belum menerapkannya secara langsung.
    Selanjutnya, program ini mengimplementasikan dua algoritma pengurutan, yaitu Bubble Sort dan Quick Sort. Bubble Sort itu cukup sederhana, tapi sayangnya tidak efisien, terutama untuk dataset yang lebih besar, karena kompleksitasnya O(n²). Di sisi lain, Quick Sort jauh lebih cepat dengan rata-rata kompleksitas O(n log n), jadi kita bisa mengharapkan performa yang lebih baik saat mengurutkan angka-angka ini.
    Program ini juga mengukur waktu eksekusi untuk masing-masing algoritma dan mencetak hasilnya, sehingga kita bisa membandingkan seberapa cepat masing-masing algoritma bekerja. Setelah proses pengurutan, program ini menampilkan klasifikasi angka-angka yang dihasilkan, jadi kita bisa lihat mana yang genap dan mana yang ganjil. Di akhir, total waktu eksekusi untuk seluruh program juga dicetak, memberikan gambaran menyeluruh tentang kinerja program dari awal sampai akhir.
Secara keseluruhan, kode ini menunjukkan bagaimana cara mengacak angka, mengurutkannya dengan dua metode berbeda, dan melakukan klasifikasi sederhana. Ini memberi kita pemahaman yang lebih baik tentang efisiensi algoritma yang digunakan, di mana Quick Sort jelas lebih cepat dibandingkan Bubble Sort. 
<h4>Devide & Conquer</h4>
    Program ini adalah contoh yang bagus untuk memahami dan membandingkan dua algoritma pengurutan dan algoritma search yang sering digunakan, yaitu Bubble Sort dan Quick Sort, serta merupakan implementasi dari prinsip “divide and conquer”. Pertama, kita menghasilkan 50 angka acak unik dalam rentang 1 hingga 100 menggunakan random.sample dan random.seed(42) untuk memastikan hasil yang konsisten.
    Bubble Sort mudah dipahami tetapi tidak efisien, dengan kompleksitas waktu O(n^2) dalam kasus terburuk. Best case-nya terjadi ketika array sudah terurut, di mana algoritma hanya perlu melakukan satu iterasi, sehingga waktu kompleksitasnya menjadi O(n). Sementara itu, Quick Sort jauh lebih efisien dengan kompleksitas waktu rata-rata O(n log n). Best case-nya terjadi ketika pivot membagi array menjadi dua bagian yang hampir sama besar, juga menghasilkan O(n log n).
    Ketika diuji, Quick Sort biasanya lebih cepat dibandingkan Bubble Sort, terutama untuk dataset yang lebih besar. Program ini menunjukkan angka acak yang dihasilkan, hasil pengurutan, dan waktu eksekusi masing-masing algoritma. Dengan ini, kita bisa melihat bahwa Quick Sort lebih unggul dalam efisiensi pengurutan.


