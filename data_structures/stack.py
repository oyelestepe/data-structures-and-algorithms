# Stack (yığın), LIFO (Last In, First Out) prensibiyle çalışan bir veri yapısıdır. 
# En son eklenen eleman, en önce çıkarılır. Stack, günlük hayatta bir yığın tabak veya kitapları düşünebiliz: en üste koyduğunuz tabağı veya kitabı en önce alırsınız.

# Temel İşlemler:
# Push: Yığına eleman ekler.
# Pop: Yığından eleman çıkarır.
# Peek (veya Top): Yığının en üstündeki elemana bakar (çıkarmaz).
# IsEmpty: Yığının boş olup olmadığını kontrol eder.

    # Stack'in Avantajları
# Push, pop ve peek işlemleri O(1) zaman karmaşıklığına sahiptir.
# LIFO prensibi sayesinde birçok problemde kolayca kullanılabilir.
    # Stack'in Dezavantajları
# Sadece en üstteki elemana erişim sağlanır. Diğer elemanlara doğrudan erişim yoktur.
# Stack boyutu dinamik olarak büyüyebilir, ancak bu durumda bellek kullanımı artar.

# Stack'in Kullanım Alanları
# Fonksiyon Çağrıları: Programlarda fonksiyonların çağrılma sırası stack ile yönetilir.
# Geri Alma (Undo) İşlemleri: Örneğin, bir metin editöründe yapılan işlemler stack ile takip edilir.
# Parantez Eşleştirme: Matematiksel ifadelerde parantezlerin doğru kapatılıp kapatılmadığını kontrol eder.
# Yol Bulma Algoritmaları: Örneğin, DFS (Depth First Search) algoritması stack kullanır.

class Stack:
    def __init__(self):
        self.stack = []  # Stack'i bir liste olarak tut

    def push(self, item):
        """Stack'e eleman ekler."""
        self.stack.append(item)

    def pop(self):
        """Stack'ten eleman çıkarır."""
        if not self.is_empty():
            return self.stack.pop()
        return None  # Stack boşsa None döndür

    def peek(self):
        """Stack'in en üstündeki elemana bakar."""
        if not self.is_empty():
            return self.stack[-1]
        return None  # Stack boşsa None döndür

    def is_empty(self):
        """Stack'in boş olup olmadığını kontrol eder."""
        return len(self.stack) == 0

    def __str__(self):
        """Stack'i string olarak gösterir."""
        return str(self.stack)

# Örnek Kullanım
if __name__ == "__main__":
    s = Stack()

    # Stack'e eleman ekle
    s.push(10)
    s.push(20)
    s.push(30)

    print("Stack:", s)  # [10, 20, 30]

    # Stack'in en üstündeki elemana bak
    print("Peek:", s.peek())  # 30

    # Stack'ten eleman çıkar
    print("Pop:", s.pop())  # 30
    print("Stack:", s)  # [10, 20]

    # Stack boş mu?
    print("Is Empty:", s.is_empty())  # False

#     Stack'in Zaman Karmaşıklıkları
# Push: O(1) (Listenin sonuna eleman ekleme)
# Pop: O(1) (Listenin sonundan eleman çıkarma)
# Peek: O(1) (Listenin son elemanına erişim)
# IsEmpty: O(1) (Listenin uzunluğunu kontrol etme)
