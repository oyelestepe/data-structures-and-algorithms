#           Arrayin Temel Özellikleri
# Hızlı Erişim: Array'deki herhangi bir elemana indeks numarasıyla doğrudan erişilebilir (O(1) zaman karmaşıklığı).
# Arrayler genellikle aynı türdeki verileri saklar (tüm elemanlar integer veya string olmalı).

# Bir array (liste) oluşturma
my_array = [10, 20, 30, 40, 50]

# Arrayin elemanlarına erişim (O(1) zaman karmaşıklığı)
print("Arrayin ilk elemanı:", my_array[0])  # 10
print("Array'in üçüncü elemanı:", my_array[2])  # 30

# Arrayin uzunluğunu bulma
print("Arrayin uzunluğu:", len(my_array))  # 5

# Arraye yeni eleman ekleme
my_array.append(60)
print("Yeni eleman eklendi:", my_array)  # [10, 20, 30, 40, 50, 60]

# Arrayden eleman silme
my_array.remove(30)
print("30 elemanı silindi:", my_array)  # [10, 20, 40, 50, 60]

# Arrayi döngü ile gezme
print("Arrayin elemanları:")
for element in my_array:
    print(element)

# Arrayin Zaman Karmaşıklıkları
# Erişim: O(1) (Doğrudan indeksle erişim)
# Arama: O(n) (Array'in tüm elemanlarını kontrol etme)
# Ekleme/Silme: O(n) (Elemanların kaydırılması gerekebilir)

def find_element(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return f"{target} elemanı {i}. indekste bulundu."
    return f"{target} elemanı dizide bulunamadı."

# Örnek
my_array = [10, 20, 30, 40, 50]
print(find_element(my_array, 30))  # 30 elemanı 2. indekste bulundu.
print(find_element(my_array, 60))  # 60 elemanı dizide bulunamadı.