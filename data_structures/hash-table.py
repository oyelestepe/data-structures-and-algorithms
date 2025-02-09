# Hash table, key-value çiftlerini depolamak için kullanılan bir veri yapısıdır. 
# Hızlı veri erişimi sağlar (ortalama O(1) zaman karmaşıklığı). Örneğin, bir sözlük gibi düşünebilirsiniz: kelime (key) ararız ve karşılığında anlamını (value) alırız.

# Hash Table Nasıl Çalışır?
# Hash Fonksiyonu: Anahtarı (key) bir indekse dönüştürür.
# Örneğin, hash("elma") → 3 gibi.

# Bu indekse karşılık gelen bellek alanına değer (value) yerleştirilir.
# Çakışma (Collision) Çözümü: Farklı anahtarlar aynı indekse düşerse, çakışmayı çözmek için linked list veya açık adresleme gibi yöntemler kullanılır.

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # Çakışmalar için iç içe listeler

    def _hash(self, key):
        """Anahtarı bir indekse dönüştürür."""
        return hash(key) % self.size  # Basit bir hash fonksiyonu

    def put(self, key, value):
        """Anahtar-değer çiftini ekler."""
        index = self._hash(key)
        # Aynı anahtar varsa güncelle, yoksa ekle
        for kv in self.table[index]:
            if kv[0] == key:
                kv[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        """Anahtara karşılık gelen değeri döndürür."""
        index = self._hash(key)
        for kv in self.table[index]:
            if kv[0] == key:
                return kv[1]
        return None  # Anahtar bulunamazsa

    def __str__(self):
        """Hash tablosunu string olarak gösterir."""
        return str(self.table)

# Örnek 
if __name__ == "__main__":
    ht = HashTable()

    ht.put("elma", 50)
    ht.put("muz", 30)
    ht.put("üzüm", 20)
    ht.put("elma", 100)  # "elma"nın değerini günceller

    print("Hash Tablosu:", ht)
    print("Elma'nın fiyatı:", ht.get("elma"))  # 100
    print("Çilek'in fiyatı:", ht.get("çilek"))  # None

    # Hash Table'ın Avantajları
# Ortalama O(1) zaman karmaşıklığı.
# Anahtar-değer çiftleri dinamik olarak eklenip silinebilir.

    # Hash Table'ın Dezavantajları
# Çakışmalar: Kötü bir hash fonksiyonu, performansı düşürür (O(n)'e yaklaşır).
# Fazla bellek alanı gerekebilir.