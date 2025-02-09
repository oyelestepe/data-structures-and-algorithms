# Queue, FIFO (First In, First Out) prensibiyle çalışan bir veri yapısıdır. 
# İlk eklenen eleman, ilk çıkarılır. Queue, günlük hayatta bir market kuyruğu gibi düşünülebilir: ilk gelen müşteri, ilk önce işini halleder.

    # Queue'in Temel Özellikleri
# FIFO (First In, First Out): İlk eklenen eleman, ilk çıkarılır.

# Temel İşlemler:
# Enqueue: Kuyruğa eleman ekler.
# Dequeue: Kuyruktan eleman çıkarır.
# Front (veya Peek): Kuyruğun önündeki elemana bakar (çıkarmaz).
# IsEmpty: Kuyruğun boş olup olmadığını kontrol eder.

# Queue'in Kullanım Alanları
# İşlem Sıralama: Yazıcıya gönderilen belgelerin sırayla işlenmesi.
# Veri Buffering: Veri akışlarında geçici depolama için kullanılır.
# BFS (Breadth First Search) Algoritması: Graf gezinme algoritmalarında kullanılır.
# Mesaj Kuyrukları: İletişim sistemlerinde mesajların sırayla işlenmesi.

        # Queue'in Avantajları
# Enqueue, dequeue ve front işlemleri O(1) zaman karmaşıklığına sahiptir.
# FIFO prensibi sayesinde birçok problemde kolayca kullanılabilir.

        # Queue'in Dezavantajları
# Sadece ön ve arka elemanlara erişim sağlanır. Diğer elemanlara doğrudan erişim yoktur.
# Queue boyutu dinamik olarak büyüyebilir, ancak bu durumda bellek kullanımı artar.

class Queue:
    def __init__(self):
        self.queue = []  # Queue'yu bir liste olarak tut

    def enqueue(self, item):
        """Queue'ya eleman ekler."""
        self.queue.append(item)

    def dequeue(self):
        """Queue'dan eleman çıkarır."""
        if not self.is_empty():
            return self.queue.pop(0)  # Listenin başından eleman çıkar
        return None  # Queue boşsa None döndür

    def front(self):
        """Queue'nun önündeki elemana bakar."""
        if not self.is_empty():
            return self.queue[0]
        return None  # Queue boşsa None döndür

    def is_empty(self):
        """Queue'nun boş olup olmadığını kontrol eder."""
        return len(self.queue) == 0

    def __str__(self):
        """Queue'yu string olarak gösterir."""
        return str(self.queue)

# Örnek Kullanım
if __name__ == "__main__":
    q = Queue()

    # Queue'ya eleman ekle
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    print("Queue:", q)  # [10, 20, 30]

    # Queue'nun önündeki elemana bak
    print("Front:", q.front())  # 10

    # Queue'dan eleman çıkar
    print("Dequeue:", q.dequeue())  # 10
    print("Queue:", q)  # [20, 30]

    # Queue boş mu?
    print("Is Empty:", q.is_empty())  # False


# Queue'in Zaman Karmaşıklıkları
# Enqueue: O(1) (Listenin sonuna eleman ekleme)
# Dequeue: O(1) (Listenin başından eleman çıkarma)
# Front: O(1) (Listenin ilk elemanına erişim)
# IsEmpty: O(1) (Listenin uzunluğunu kontrol etme)