# Binary search, sıralı bir listede belirli bir elemanı bulmak için kullanılan verimli bir arama algoritmasıdır. 
# Algoritma, listenin ortasındaki elemanı kontrol eder ve aranan elemana göre listenin sol veya sağ yarısına odaklanır. 
# Bu işlem, eleman bulunana veya liste tükenene kadar tekrarlanır.

# Binary Search Nasıl Çalışır?
# Listenin ortasındaki elemanı kontrol et.
# Eğer ortadaki eleman aranan elemansa, işlemi sonlandır.
# Eğer aranan eleman ortadaki elemandan küçükse, listenin sol yarısına odaklan.
# Eğer aranan eleman ortadaki elemandan büyükse, listenin sağ yarısına odaklan.
# Bu işlemi, eleman bulunana veya liste tükenene kadar tekrarla.

# Sıralama algoritmaları ile arama algoritmaları arasındaki en büyük fark, sıralama algoritmalarının diziyi değiştirmesi, arama algoritmalarının ise diziyi olduğu gibi bırakmasıdır.

# Binary Search Zaman Karmaşıklığı
# En İyi Durum: O(1) (Aranan eleman tam ortadaysa)
# En Kötü Durum: O(log n) (Aranan eleman listede yoksa veya listenin sonunda ise)
# Ortalama Durum: O(log n)

def binary_search(arr, target):
    left, right = 0, len(arr) - 1  # Listenin başlangıç ve bitiş indeksleri

    while left <= right:
        mid = (left + right) // 2  # Listenin ortasındaki indeks
        if arr[mid] == target:  # Aranan eleman bulundu
            return mid
        elif arr[mid] < target:  # Aranan eleman sağ yarıda
            left = mid + 1
        else:  # Aranan eleman sol yarıda
            right = mid - 1

    return -1  # Eleman bulunamazsa -1 döndür

# Örnek Kullanım
if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    target = 9

    result = binary_search(arr, target)

    if result != -1:
        print(f"{target} elemanı {result}. indekste bulundu.")
    else:
        print(f"{target} elemanı listede bulunamadı.")