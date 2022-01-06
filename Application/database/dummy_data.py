from Application.database.model import *


try:
    os.remove("data.sqlite")
except FileNotFoundError:
    print('db not found')
Base.metadata.create_all(bind=engine)

food_categories = {
    "Pastas": ["Spaghetti Nappolitana", "Spaoghetti Carbonara"],
    "Pizza Corner": ["Margareta", "Oasis 24-7 Deluxe Pizza","Hawii PIzza","Regina Pizza", "Vegetarian Pizza", "Chicken Pizza", ],
    "Beverage": ["African Tea or Coffee", "Black Tea or Coffee", "Hot Chocalate", "English Tea or Coffee", "Glass of Hot Milk"],
    "Juices": ["Pineapple Juice", "Water Melon", "Cocktail Juice", "Frute Platter"],
    "Burgers": ["Beef Burger", "Chicken Burger", "Vegetable Burger", "Cheese Burger", "Egg Burger"],
    "Sandwiches": ["Chicken Sandwich", "Beef sandwich", "Egg sandwich", "Cheeses sandwich"],
    "Chicken Tatys": ["Grilled Chicken Chips", "Garlic Chicken Chips", "Chicken Stew"],
    "Beef or Goat": ["Beef Stir-fry"],
    "Oasis Mixed Grill": ["OX Liver"],
    "Goat": ["Pan Fried Goat", "Goat Stew"],
    "Fish": ["Fish Tillet", "Fish Fingers"],
    "Snacks": ["Beef Samosa", "Vegetable Samosa", "Chicken Wings", "Chips Plain", "Chips Masala", "Chicken Drum Stick", "Egg Plain", "Chapati", "Mandazi", "G.nuts"],
    "Salad": ["Garden Salad", "Chef Salad"],
    "Soups": ["Cream of Tomato Soup", "Cream of Mushroom", "Chicken Clear Soup", "Beans Sauce", "Pork Plain", "Chicken Plain", "Goat Plain"]
}

brand_categories = {
    "Beer or AFBs": ["Nile Special 500ml", "Nile Special 330ml", "Club Pilsner 500ml", "Club Pilsner 330ml", "Club Twist 330ml", "Eagle Dark 300ml", "Castle Lager 440ml", "Castle Lite 330ml", "Castle Milk Stout 330ml", "Redds Preminum", "Ice Double Black", "Bell Lager", "Guiness 500ml", "Smirnoff Red", "Smirnoff Black"],
    "Energy Drink" : ["Red Bull", "String", "Alvaro", "Coke", "Pepsi", "Coke Plastic 500ml"],
    "Wines and Wisky": ["Red Wines Sweet", "Red Wine", "White Wine Sweet", "White Wine Dry", "Zappa Red", "Zappa Green" "Tequilla", "Amanla", "MC Dowels", "Captain Morgan", "South Comfort", "Four Cousins", "Baileys"],
    "Red Label": ["Red Label", "Red Label 200ml", "Red Label 350ml", "Red Label 750ml", "Red Label 1 Litre"],
    "Black Label": ["Black Label", "Black Label 200ml", "Black Label 350ml", "Black Label 750ml", "Black Label 1 Litre"],
}


Manager
user = User("samit", "123")
manager = Manager("Samuel", "Itwaru", "samuelitwaru@yahoo.com", "samuelitwaru@yahoo.com", user)

# Cashier
user2 = User("josh", "123")
cashier = Cashier("Byenkya", "Joshua", user2)

# Chef
user3 = User("mutesi", "123")
chef = Chef("Mutesi", "Wilbrod", True, user3)

# Waiter
waiter = Waiter("Okot", "Smith")

# Kitchen Stock
kitchen_stock = [("Ginger", "Kilograms"), ("Oil", "Litres"), ("Tomatoes", "Pieces"), ("Onions", "Pieces"), ("Cabbage", "Heads")]
for name, usage_unit in kitchen_stock:
    KitchenStock(name, usage_unit)

# Food Categories
for food_category, foods in food_categories.items():
    cat = FoodCategory(food_category)
    for food in foods:
        Food(food, choice(range(15, 100)), "Plate", choice(range(1000, 40000, 500)), cat)

# Drink Categories
for drink_category, brands in brand_categories.items():
    cat = Category(drink_category)
    for brand in brands:
        price = choice(range(1000, 20000, 500))
        pg = PurchaseGuide("Bottle", price)
        brand = Brand(brand, choice(range(15, 100)), cat, pg)
        sg = SaleGuide("Bottle", price + 1000, 10, brand)

session.close()
