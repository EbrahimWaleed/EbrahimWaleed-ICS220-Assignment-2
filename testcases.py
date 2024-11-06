from classes import *
# Test cases for the Great E-books Store application

# Test Customer class
print("Testing Customer class...")
customer = Customer("John Doe", "john.doe@example.com", True)
# Expected: Customer(name=John Doe, loyalty_member=True)
print(customer)
assert customer.get_name() == "John Doe"
assert customer.get_contact_info() == "john.doe@example.com"
assert customer.is_loyalty_member() == True
customer.set_contact_info("john.updated@example.com")
assert customer.get_contact_info() == "john.updated@example.com"
customer.set_loyalty_member(False)
assert customer.is_loyalty_member() == False

# Test Discount class
print("\nTesting Discount class...")
discount = Discount(0.1, 0.2)
assert discount.apply_loyalty_discount(True) == 0.1
assert discount.apply_loyalty_discount(False) == 0
assert discount.apply_bulk_discount(5) == 0.2
assert discount.apply_bulk_discount(3) == 0
# Expected: Discount(loyalty_discount=0.1, bulk_discount=0.2)
print(discount)

# Test Product and Ebook classes
print("\nTesting Product and Ebook classes...")
ebook = Ebook("The Great Gatsby", "F. Scott Fitzgerald", "1925", "Fiction", 10.99)
assert ebook.get_title() == "The Great Gatsby"
assert ebook.get_price() == 10.99
assert ebook.get_author() == "F. Scott Fitzgerald"
assert ebook.get_publication_date() == "1925"
assert ebook.get_genre() == "Fiction"
# Expected: Ebook(title=The Great Gatsby, author=F. Scott Fitzgerald, genre=Fiction, price=10.99)
print(ebook)

# Test OrderItem class
print("\nTesting OrderItem class...")
order_item = OrderItem(ebook, 3)
assert order_item.get_ebook() == ebook
assert order_item.get_quantity() == 3
assert order_item.get_total_price() == 32.97  # 10.99 * 3
order_item.set_quantity(5)
assert order_item.get_quantity() == 5
assert order_item.get_total_price() == 54.95  # 10.99 * 5
# Expected: OrderItem(ebook=The Great Gatsby, quantity=5, total_price=54.95)
print(order_item)

# Test ShoppingCart class
print("\nTesting ShoppingCart class...")
cart = ShoppingCart()
cart.add_item(order_item)
assert len(cart.get_items()) == 1
assert cart.get_items()[0].get_total_price() == 54.95
cart.remove_item(order_item)
assert len(cart.get_items()) == 0
# Expected: ShoppingCart(items=)
print(cart)

# Test Order class
print("\nTesting Order class...")
cart.add_item(order_item)
customer.set_loyalty_member(True)
# Apply loyalty discount and VAT
order = Order(customer, cart.get_items(), discount.apply_loyalty_discount(customer.is_loyalty_member()))
assert order.get_total_price() == (54.95 * (1 - 0.1) * 1.08)
# Expected: Order with customer name, total price, and order items
print(order)

# Additional test cases for discounts
print("\nTesting bulk discounts...")
# Bulk purchase
bulk_item = OrderItem(ebook, 6)
cart = ShoppingCart()
cart.add_item(bulk_item)
order_with_bulk_discount = Order(
    customer,
    cart.get_items(),
    discount.apply_bulk_discount(bulk_item.get_quantity())
)

assert order_with_bulk_discount.get_total_price() == (bulk_item.get_total_price() * (1 - 0.2) * 1.08)
# Expected: Order with bulk discount applied
print(order_with_bulk_discount)

print("\nAll tests passed!")
