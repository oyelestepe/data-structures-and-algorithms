# Linked list, verilerin düğümler (nodes) halinde saklandığı bir veri yapısıdır. Her düğüm iki kısımdan oluşur:
    # Data: Düğümde saklanan veri (sayı, metin, nesne).
    # Next: Bir sonraki düğümü işaret eden referans (pointer).

        # Linked List'in Avantajları
#Eleman ekleme/silme işlemleri kolaydır. Özellikle listenin başına veya ortasına eleman ekleme/silme işlemleri dizilere göre daha verimlidir.

        # Linked List'in Dezavantajları
# Belirli bir indeksteki elemana erişmek için tüm liste taranmalıdır.
# Her düğüm, bir sonraki düğümü işaret etmek için ekstra bellek kullanır.


# Düğüm (Node)
class Node:
    def __init__(self, data):
        self.data = data  # Düğümde saklanan veri
        self.next = None  # Bir sonraki düğümü işaret eden referans

# Linked List
class LinkedList:
    def __init__(self):
        self.head = None  # Listenin başlangıç düğümü

    # Listenin sonuna eleman ekleme
    def append(self, data):
        new_node = Node(data)  # Yeni bir düğüm oluştur
        if not self.head:  # Eğer liste boşsa
            self.head = new_node  # Yeni düğümü başlangıç yap
            return
        # Listenin sonuna git
        current = self.head
        while current.next:
            current = current.next
        # Yeni düğümü ekle
        current.next = new_node

    # Listeyi yazdırma
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Örnek
if __name__ == "__main__":
    # Linked List oluştur
    ll = LinkedList()

    # Eleman ekle
    
    ll.append(10)
    ll.append(20)
    ll.append(30)

    # Listeyi yazdır
    ll.print_list()


    # Linked List'in Zaman Karmaşıklıkları
# Ekleme (Append): Listenin sonuna ekleme: O(n)
# Listenin başına ekleme: O(1)
# Silme (Delete): Belirli bir değeri silme: O(n)
# Arama (Search): O(n)
# Erişim (Access): O(n) (Dizilerde O(1))