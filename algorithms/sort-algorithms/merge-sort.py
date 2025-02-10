# Merge sort, böl ve yönet (divide and conquer) mantığıyla çalışan bir sıralama algoritmasıdır. 
# Algoritma, listeyi sürekli ikiye böler, her parçayı ayrı ayrı sıralar ve daha sonra bu sıralanmış parçaları birleştirir. 
# Bu yaklaşım, özellikle büyük veri setleri için oldukça verimlidir.

    # Merge Sort Nasıl Çalışır?
# Liste, tek eleman kalana kadar sürekli ikiye bölünür.
# Her parça ayrı ayrı sıralanır.
# Sıralanmış parçalar, doğru sırayla birleştirilir.

# Merge Sort'un Avantajları
# Her durumda O(n log n) zaman karmaşıklığı.
# Aynı değere sahip elemanların sırası değişmez.
# Büyük listeler için idealdir.

# Merge Sort'un Dezavantajları
# Birleştirme işlemi sırasında ek bellek gerektirir.
# Küçük listeler için daha basit algoritmalar (insertion sort) daha verimli olabilir.

# Merge Sort Zaman Karmaşıklığı
# En İyi Durum: O(n log n)
# En Kötü Durum: O(n log n)
# Ortalama Durum: O(n log n)
# Merge sort, her durumda O(n log n) zaman karmaşıklığına sahiptir, bu da onu büyük veri setleri için oldukça verimli kılar.

def merge_sort(arr):
    # Temel durum: Liste zaten sıralı veya boşsa
    if len(arr) <= 1:
        return arr

    # Listeyi ikiye böl
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])  # Sol yarı
    right_half = merge_sort(arr[mid:])  # Sağ yarı

    # İki sıralanmış yarıyı birleştir
    return merge(left_half, right_half)

def merge(left, right):
    sorted_array = []
    i = j = 0

    # İki listeyi karşılaştırarak birleştir
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    # Kalan elemanları ekle (eğer varsa)
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])

    return sorted_array

# Örnek Kullanım
if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    print("Sıralanmamış liste:", arr)

    sorted_arr = merge_sort(arr)
    print("Sıralanmış liste:", sorted_arr)
