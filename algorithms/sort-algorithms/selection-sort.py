# Selection sort, bir listedeki en küçük elemanı bulup onu listenin başına yerleştirerek çalışan bir sıralama algoritmasıdır. 
# Bu işlem, listenin sıralanmamış kısmı için tekrarlanır.

# Selection Sort Nasıl Çalışır?
# Listenin sıralanmamış kısmında en küçük elemanı bul.
# Bu elemanı, sıralanmamış kısmın başındaki elemanla yer değiştir.
# Sıralanmış kısmı bir eleman genişlet ve sıralanmamış kısmı bir eleman daralt.
# Bu işlemi, liste sıralanana kadar tekrarla.

# Selection Sort'un Avantajları
# Basit ve Anlaşılır: Küçük listeler için idealdir.
# Yerinde Sıralama: Ek bellek gerektirmez.

# Selection Sort'un Dezavantajları
# Yavaş: Büyük listeler için O(n²) zaman karmaşıklığı nedeniyle verimsizdir.
# Çok Fazla Karşılaştırma: Her geçişte çok sayıda karşılaştırma yapılır.

# Selection sort, her durumda O(n²) zaman karmaşıklığına sahiptir.
# En İyi Durum: O(n²)
# En Kötü Durum: O(n²)
# Ortalama Durum: O(n²)

def selection_sort(arr):
    n = len(arr)
    for i in range(n):  # Her geçişte bir eleman doğru yerine yerleşir
        min_idx = i  # Sıralanmamış kısmın en küçük elemanının indeksi
        for j in range(i + 1, n):  # Sıralanmamış kısmı gez
            if arr[j] < arr[min_idx]:  # Daha küçük bir eleman bulundu
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Yer değiştir

# Örnek 
if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    print("Sıralanmamış liste:", arr)

    selection_sort(arr)
    print("Sıralanmış liste:", arr)
