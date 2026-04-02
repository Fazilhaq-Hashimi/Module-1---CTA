# ItemToPurchase Class to support the ShoppingCart
class ItemToPurchase:
    def __init__(self, name="none", price=0, quantity=0, description="none"):
        self.item_name = name
        self.item_price = price
        self.item_quantity = quantity
        self.item_description = description

# Step 4: Build the ShoppingCart class
class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, item_to_modify):
        found = False
        for item in self.cart_items:
            if item.item_name == item_to_modify.item_name:
                found = True
                # Only change values if they aren't the default "empty" values
                if item_to_modify.item_description != "none":
                    item.item_description = item_to_modify.item_description
                if item_to_modify.item_price != 0:
                    item.item_price = item_to_modify.item_price
                if item_to_modify.item_quantity != 0:
                    item.item_quantity = item_to_modify.item_quantity
                break
        if not found:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        total_quantity = 0
        for item in self.cart_items:
            total_quantity += item.item_quantity
        return total_quantity

    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += (item.item_price * item.item_quantity)
        return total_cost

    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                cost = item.item_price * item.item_quantity
                print(f"{item.item_name} {item.item_quantity} @ ${item.item_price} = ${cost}")
        
        print(f"Total: ${self.get_cost_of_cart()}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("\nItem Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")

# Step 5 & 6: Menu Logic
def print_menu(cart):
    menu = (
        "\nMENU\n"
        "a - Add item to cart\n"
        "r - Remove item from cart\n"
        "c - Change item quantity\n"
        "i - Output items' descriptions\n"
        "o - Output shopping cart\n"
        "q - Quit\n"
    )
    
    choice = ''
    while choice != 'q':
        print(menu)
        choice = input("Choose an option: ").lower()
        
        if choice == 'a':
            print("\nADD ITEM TO CART")
            name = input("Enter the item name: ")
            desc = input("Enter the item description: ")
            price = int(input("Enter the item price: "))
            qty = int(input("Enter the item quantity: "))
            new_item = ItemToPurchase(name, price, qty, desc)
            cart.add_item(new_item)
            
        elif choice == 'r':
            print("\nREMOVE ITEM FROM CART")
            name = input("Enter name of item to remove: ")
            cart.remove_item(name)
            
        elif choice == 'c':
            print("\nCHANGE ITEM QUANTITY")
            name = input("Enter the item name: ")
            qty = int(input("Enter the new quantity: "))
            # We create a temp item with default price/desc so they don't get changed
            modify_me = ItemToPurchase(name=name, quantity=qty)
            cart.modify_item(modify_me)
            
        elif choice == 'i':
            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()
            
        elif choice == 'o':
            print("\nOUTPUT SHOPPING CART")
            cart.print_total()

# Main Section
if __name__ == "__main__":
    cust_name = input("Enter customer's name: ")
    today_date = input("Enter today's date: ")
    print(f"Customer name: {cust_name}")
    print(f"Today's date: {today_date}")
    
    my_cart = ShoppingCart(cust_name, today_date)
    print_menu(my_cart)
