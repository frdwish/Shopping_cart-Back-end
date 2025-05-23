🔍 Problem Statement
In traditional terminal-based applications, user interaction can feel dry and overwhelming, especially for beginners. This project aimed to:
Provide a simple yet engaging shopping experience in a terminal.
Allow customers to add, remove, view, and purchase food items.
Include interactive visual feedback to improve user engagement (like animated loading).
Practice Python OOP concepts such as classes, methods, encapsulation, and loops.


Objectives
Create a ShoppingCart class with methods and attributes.
Add dynamic user interaction using input() loops.
Improve user experience with animated loaders (time.sleep, sys.stdout.write).
Make the interface clear with emojis and formatting.



🧱 Project Structure
Component	Description
food_items	Dictionary storing food item names and prices.
__init__()	Initializes the shop and customer.
animated_loading()	Displays a smooth loading animation in the terminal.
show_menu()	Fetches and displays the full food menu.
shoppingcart()	Core logic handling user input and operations.



🧠 Key Features
Feature	Description
🛒 Add Product	User selects items to add to cart; checks for valid input.
🗑️ Remove Product	Allows deletion of items already in cart.
📦 View Cart	Shows current items and total price.
💤 Loading Animation	Simulates fetching or processing data to improve experience.
🧠 Input Validation	Checks for invalid inputs and guides users.