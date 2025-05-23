import time
import sys

class ShoppingCart:

    food_items = {
        "Paneer Butter Masala": 180,
        "Chicken Biryani": 220,
        "Veg Burger": 90,
        "Masala Dosa": 70,
        "Margherita Pizza": 150,
        "French Fries": 60,
        "Egg Roll": 80,
        "Cold Coffee": 100,
        "Gulab Jamun (2 pcs)": 40,
        "Chicken Momos": 120
    }

    def __init__(self, shopname, customername):
        self.shopname = shopname
        self.customername = customername
        self.cart = []

    def animated_loading(self, message="Loading"):
        for _ in range(3):
            for dot in "...":
                sys.stdout.write(f"\r{message}{dot}")
                sys.stdout.flush()
                time.sleep(0.2)
        print("\r" + " " * (len(message)+3), end="\r")  # clear line

    def show_menu(self):
        self.animated_loading("Fetching menu")
        time.sleep(0.3)
        print("<---🍱 THIS IS OUR MENU --->🍔")
        for item, price in self.food_items.items():
            print(f"{item} - ₹{price}")
        print()

    def shoppingcart(self):
        def welcome_box(message):
         length = len(message)
         print("+" + "-" * (length + 4) + "+")
         print("|" + " " * (length + 4) + "|")
         print(f"|  {message}  |")
         print("|" + " " * (length + 4) + "|")
         print("+" + "-" * (length + 4) + "+")

# Example usage
        welcome_box("Welcome to GaribKiDukan!")
        # print(f"\nWELCOME {self.customername.upper()} TO {self.shopname.upper()} 😊")
        print("🛒 Please wait while we prepare your shopping experience 🛒\n")
        self.animated_loading("Starting")
        time.sleep(0.3)

        while True:
            self.show_menu()
            print("<--- SELECT OPTION -->")
            print("1. Add Product")
            print("2. Remove Product")
            print("3. Show Cart")
            print("4. Exit")

            choice = input("--> ")

            if choice == "1":
                try:
                    n = int(input("How many food items do you want to add? "))
                    for _ in range(n):
                        while True:
                            item = input("Enter the product name: ")
                            if item in self.food_items:
                                self.cart.append(item)
                                print(f"✅ {item} added to cart 🛒\n")
                                break
                            else:
                                print("❌ Invalid item. Please enter again.\n")
                except ValueError:
                    print("❗ Please enter a valid number.\n")

            elif choice == "2":
                item = input("Enter the product name to remove: ")
                if item in self.cart:
                    self.cart.remove(item)
                    print(f"🗑️ {item} removed from cart.\n")
                else:
                    print("⚠️ Item not found in cart.\n")

            elif choice == "3":
                if self.cart:
                    print(f"\n🧾 Your Cart: {self.cart}")
                    total = sum(self.food_items[item] for item in self.cart)
                    print(f"💰 Total Price: ₹{total}\n")
                else:
                    print("🛒 Your cart is empty.\n")

            elif choice == "4":
                ask = input("Type 'exit' to leave the store: ")
                if ask.lower() == 'exit':
                    self.animated_loading("Logging out")
                    print("👋 Thank you for visiting! Come again.")
                    break
            else:
                print("⚠️ Invalid choice. Try again.\n")


# Run the program
details = ShoppingCart("GaribKiDukan", "Fardwish")
details.shoppingcart()
