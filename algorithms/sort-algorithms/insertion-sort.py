# Insertion sort, basit bir sıralama algoritmasıdır. 
# Kartları sıralama gibi düşünebilirsiniz: elinizdeki kartları tek tek alır ve doğru yere yerleştirirsiniz. Algoritma, listenin sıralı kısmını adım adım genişleterek çalışır.

    # Insertion Sort Nasıl Çalışır?
# Listenin ilk elemanını sıralı kabul eder.
# Sonraki elemanları tek tek alır ve sıralı kısımda doğru yere yerleştirir.
# Bu işlemi tüm liste sıralanana kadar tekrarlar.

    # Insertion Sort'un Avantajları
# Basit ve Anlaşılır: Küçük listeler için idealdir.
# Yerinde Sıralama: Ek bellek gerektirmez.
# Adaptif: Liste zaten kısmen sıralıysa hızlı çalışır.

    # Insertion Sort'un Dezavantajları
# Yavaş: Büyük listeler için O(n²) zaman karmaşıklığı nedeniyle verimsizdir.
# Çok Fazla Karşılaştırma: Her eleman için çok sayıda karşılaştırma yapılır.


    # Insertion Sort Zaman Karmaşıklığı
# En Kötü Durum: O(n²) (Liste tersten sıralıysa)
# En İyi Durum: O(n) (Liste zaten sıralıysa)
# Ortalama Durum: O(n²)

def insertion_sort(arr):
    # Listenin her elemanını gez
    for i in range(1, len(arr)):
        key = arr[i]  # Şu anki eleman
        j = i - 1  # Sıralı kısmın son indeksi

        # Sıralı kısımda doğru yeri bul
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]  # Elemanları sağa kaydır
            j -= 1

        arr[j + 1] = key  # Doğru yere yerleştir

# Örnek Kullanım
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    print("Sıralanmamış liste:", arr)

    insertion_sort(arr)
    print("Sıralanmış liste:", arr)