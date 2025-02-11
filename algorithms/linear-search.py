# Linear search, bir listede veya dizide belirli bir elemanı bulmak için kullanılan en basit arama algoritmasıdır. 
# Algoritma, listenin başından başlar ve her elemanı tek tek kontrol eder. Aranan eleman bulununca işlem sonlandırılır.

# Linear Search Nasıl Çalışır?
# Listenin başından başla.
# Her elemanı, aranan elemanla karşılaştır.
# Eşleşme bulunursa, elemanın indeksini döndür.
# Listenin sonuna kadar eşleşme bulunamazsa, elemanın listede olmadığını belirt.

# Linear Search Zaman Karmaşıklığı
# En İyi Durum: O(1) (Aranan eleman listenin ilk elemanıysa)
# En Kötü Durum: O(n) (Aranan eleman listenin sonunda veya listede yoksa)
# Ortalama Durum: O(n)

# Sıralama algoritmaları ile arama algoritmaları arasındaki en büyük fark, sıralama algoritmalarının diziyi değiştirmesi, arama algoritmalarının ise diziyi olduğu gibi bırakmasıdır.

def linear_search(arr, target):
    # Listenin her elemanını gez
    for i in range(len(arr)):
        if arr[i] == target:  # Aranan eleman bulundu
            return i  # Elemanın indeksini döndür
    return -1  # Eleman bulunamazsa -1 döndür

# Örnek
if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    target = 300

    result = linear_search(arr, target)

    if result != -1:
        print(f"{target} elemanı {result}. indekste bulundu.")
    else:
        print(f"{target} elemanı listede bulunamadı.")


# Linear Search'un Avantajları
# Küçük listeler veya sıralanmamış listeler için idealdir.
# Sıralı veya sıralanmamış listelerde çalışır.

# Linear Search'un Dezavantajları
# Büyük listeler için O(n) zaman karmaşıklığı nedeniyle verimsizdir.
# Her eleman için karşılaştırma yapılır.

def linear_search_all(arr, target):
    indices = []  # Eşleşen indeksleri tut
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)
    return indices

# Örnek Kullanım
if __name__ == "__main__":
    arr = [10, 20, 30, 20, 40, 20]
    target = 20

    result = linear_search_all(arr, target)

    if result:
        print(f"{target} elemanı şu indekslerde bulundu: {result}")
    else:
        print(f"{target} elemanı listede bulunamadı.")