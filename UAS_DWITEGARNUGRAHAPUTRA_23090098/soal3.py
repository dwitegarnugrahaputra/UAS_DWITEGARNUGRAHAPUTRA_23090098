class RestaurantQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, order):
        self.queue.append(order)
        print(f"Pesanan '{order}' telah ditambahkan ke antrian.")

    def dequeue(self):
        if self.queue:
            order = self.queue.pop(0)
            print(f"pesanan '{order}' telah dilayani.")
        else:
            print("pesanan tidak terdaftar diantrian.")

    def display_queue(self):
        if self.queue:
            print("antrian saat ini:", self.queue)
        else:
            print("antrian kosong.")

def main():
    restaurant_queue = RestaurantQueue()
    while True:
        print("\nSistem Antrian Restoran")
        print("1. tambah pesanan (Enqueue)")
        print("2. layani pesanan (Dequeue)")
        print("3. tampilkan antrian saat ini")
        print("4. keluar")

        choice = input("masukkan pilihan Anda: ")
        if choice == '1':
            order = input("masukkan pesanan yang ingin ditambahkan: ")
            restaurant_queue.enqueue(order)
        elif choice == '2':
            restaurant_queue.dequeue()
        elif choice == '3':
            restaurant_queue.display_queue()
        elif choice == '4':
            print("keluar dari program.")
            break
        else:
            print("pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
