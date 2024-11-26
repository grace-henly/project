class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_to_cart(self, product, quantity):
        self.cart.append({"product": product, "quantity": quantity})
        print(f"Added {quantity} x {product.name} to your cart.")

class OnlineStore:
    def __init__(self):
        # Produk tanpa stok, hanya nama dan harga
        self.products = [
            Product(1, "Baju", 150000),
            Product(2, "Celana", 200000),
            Product(3, "Tas", 350000)
        ]
        self.cart = ShoppingCart()

    def run(self):
        while True:
            print("\n1. View Products\n2. Add to Cart\n3. Checkout\n4. Exit")
            choice = input("Choose: ")
            if choice == "1":
                for p in self.products:
                    print(f"{p.id}. {p.name} - {p.price}")
            elif choice == "2":
                p_id = int(input("Enter Product ID: "))
                qty = int(input("Enter quantity: "))
                product = next((p for p in self.products if p.id == p_id), None)
                if product:
                    self.cart.add_to_cart(product, qty)
            elif choice == "3":
                print("Checkout successful!")
                break
            elif choice == "4":
                break

# Main program
store = OnlineStore()
store.run()
