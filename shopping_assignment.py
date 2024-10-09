class Product:
    def __init__(self, product_name, price, quantity_in_stock):
        self.product_name = product_name
        self.price = price
        self.quantity_in_stock = quantity_in_stock
        
    #display product information
    def display_product_info(self):
        print(f"product: {self.product_name}, price: {self.price}, stock: {self.quantity_in_stock}")
        
class ShoppingCart:
    total_carts = 0
    
    #shoppingCart constructor
    def __init__(self):
        self.items = []
        ShoppingCart.total_carts += 1
        
    #adding a product to cart
    def add_to_cart(self,product,quantity):
        if product.quantity_in_stock >= quantity:
            self.items.append((product, quantity))
            product.quantity_in_stock -= quantity
        else:
            print(f"Not enough tock for{product.product_name}") 
                   
    #method to remove products from the cart
    def remove_from_cart(self,product):
        self.items =[item for item in self.items if item[0] !=product]
    
    #display cart items
    def display_cart(self):
        print("Cart items:")
        for product, quantity in self.items:
            print(f"{product.product_name}: {quantity} items")
        
    #calculating total price
    def calculate_total(self):
        total = sum(product.price * quantity for product, quantity in self.items)
        return total
    
# product objects
product1 = Product("Shoes", 36000, 23)
product2 = Product("water_bottle", 6000, 27)
    
#shopping cart instances
cart1 = ShoppingCart()
cart2 = ShoppingCart()
  
# Performing a series of operations on cart1
cart1.add_to_cart(product1, 1)
cart1.add_to_cart(product2, 2)
cart1.display_cart()
print(f"Total for cart1: {cart1.calculate_total()}")

# Performing a series of operations on cart2
cart2.add_to_cart(product1, 2)
cart2.remove_from_cart(product2)
cart2.add_to_cart(product2, 1)
cart2.display_cart()
print(f"Total for cart2: {cart2.calculate_total()}")
  
    
    
                
        
        
        