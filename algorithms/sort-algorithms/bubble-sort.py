# Bubble sort, basit bir sıralama algoritmasıdır. Algoritma, listenin elemanlarını karşılaştırma ve değiştirme yöntemiyle sıralar. 
# Her adımda, yan yana duran iki eleman karşılaştırılır ve eğer sıraları yanlışsa yer değiştirilir. Bu işlem, liste sıralanana kadar tekrarlanır.

# Bubble Sort Nasıl Çalışır?
# Listenin başından başla.
# Yan yana duran iki elemanı karşılaştır.
# Eğer sıraları yanlışsa, yerlerini değiştir.
# Listenin sonuna ulaşınca, en büyük eleman doğru yerine yerleşmiş olur.
# Bu işlemi, liste sıralanana kadar tekrarla.

# Bubble Sort'un Avantajları
# Küçük listeler için idealdir.
# Ek bellek gerektirmez.

# Bubble Sort'un Dezavantajları
# Büyük listeler için O(n²) zaman karmaşıklığı nedeniyle verimsizdir.
# Her adımda çok sayıda işlem yapılır.

# Bubble Sort Zaman Karmaşıklığı
# En İyi Durum: O(n) (Liste zaten sıralıysa)
# En Kötü Durum: O(n²) (Liste tersten sıralıysa)
# Ortalama Durum: O(n²)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):  # Her geçişte bir eleman doğru yerine yerleşir
        for j in range(0, n - i - 1):  # Sıralanmamış kısmı gez
            if arr[j] > arr[j + 1]:  # Yan yana elemanları karşılaştır
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Yer değiştir

# Örnek 
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Sıralanmamış liste:", arr)

    bubble_sort(arr)
    print("Sıralanmış liste:", arr)

