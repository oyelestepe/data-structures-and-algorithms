# Quick sort, böl ve yönet (divide and conquer) mantığıyla çalışan bir sıralama algoritmasıdır. 
# Algoritma, bir pivot eleman seçer ve listeyi pivotun etrafında ikiye böler: pivotdan küçükler sola, büyükler sağa. 
# Bu işlemi her alt liste için tekrarlayarak listeyi sıralar.

# Quick Sort Nasıl Çalışır?
# Listenin bir elemanı pivot olarak seçilir (genellikle ilk, son veya rastgele bir eleman).
# Liste, pivotdan küçükler ve büyükler olarak ikiye ayrılır.
# Her iki alt liste için aynı işlem tekrarlanır.
# Sıralanmış alt listeler birleştirilir.

# Quick Sort Zaman Karmaşıklığı
# En İyi Durum: O(n log n) (Pivot her seferinde listeyi iki eşit parçaya böler)
# En Kötü Durum: O(n²) (Pivot her seferinde en küçük veya en büyük eleman seçilirse)
# Ortalama Durum: O(n log n)


def quick_sort(arr):
    # Temel durum: Liste zaten sıralı veya boşsa
    if len(arr) <= 1:
        return arr

    # Pivot seçimi (örneğin, son eleman)
    pivot = arr[-1]

    # Pivotdan küçükler ve büyükler
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]

    # Alt listeleri sırala ve birleştir
    return quick_sort(left) + [pivot] + quick_sort(right)

# Örnek
if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    print("Sıralanmamış liste:", arr)

    sorted_arr = quick_sort(arr)
    print("Sıralanmış liste:", sorted_arr)
