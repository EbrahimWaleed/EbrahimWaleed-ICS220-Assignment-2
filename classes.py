
class Customer:
    def __init__(self, name: str, contact_info: str, loyalty_member: bool = False):
        """Initialize Customer with name, contact info, and loyalty membership status."""
        self.__name = name
        self.__contact_info = contact_info
        self.__loyalty_member = loyalty_member

    # Getters
    def get_name(self):
        return self.__name

    def get_contact_info(self):
        return self.__contact_info

    def is_loyalty_member(self):
        return self.__loyalty_member

    # Setters
    def set_contact_info(self, contact_info: str):
        self.__contact_info = contact_info

    def set_loyalty_member(self, loyalty_member: bool):
        self.__loyalty_member = loyalty_member

    def __str__(self):
        return f"Customer(name={self.__name}, loyalty_member={self.__loyalty_member})"


class Discount:
    def __init__(self, loyalty_discount: float = 0.1, bulk_discount: float = 0.2):
        """Initialize Discount with loyalty and bulk discount rates."""
        self.__loyalty_discount = loyalty_discount
        self.__bulk_discount = bulk_discount

    def apply_loyalty_discount(self, is_member: bool):
        return self.__loyalty_discount if is_member else 0

    def apply_bulk_discount(self, quantity: int):
        return self.__bulk_discount if quantity >= 5 else 0

    def __str__(self):
        return f"Discount(loyalty_discount={self.__loyalty_discount}, bulk_discount={self.__bulk_discount})"

class Product:
    def __init__(self, title: str, price: float):
        """Initialize Product with title and price."""
        self._title = title
        self._price = price

    # Getters
    def get_title(self) -> str:
        return self._title

    def get_price(self) -> float:
        return self._price


class Ebook(Product):
    def __init__(self, title: str, author: str, publication_date: str, genre: str, price: float):
        """Initialize Ebook with title, author, publication date, genre, and price."""
        super().__init__(title, price)
        self.__author = author
        self.__publication_date = publication_date
        self.__genre = genre

    # Getters specific to Ebook
    def get_author(self) -> str:
        return self.__author

    def get_publication_date(self) -> str:
        return self.__publication_date

    def get_genre(self) -> str:
        return self.__genre

    def __str__(self) -> str:
        return f"Ebook(title={self._title}, author={self.__author}, genre={self.__genre}, price={self._price})"



class Order:
    VAT_RATE = 0.08  # 8% VAT

    def __init__(self, customer: 'Customer', items: list, discount: float = 0):
        """Initialize Order with customer, items, and discount."""
        self.__customer = customer
        self.__items = items
        self.__discount = discount

    def get_total_price(self):
        total = sum(item.get_total_price() for item in self.__items)
        total_after_discount = total * (1 - self.__discount)
        return total_after_discount * (1 + self.VAT_RATE)

    def __str__(self):
        item_details = "\n".join([str(item) for item in self.__items])
        return (f"Order(customer={self.__customer.get_name()}, total_price={self.get_total_price()}, items=\n{item_details})")


class OrderItem:
    def __init__(self, ebook: 'Ebook', quantity: int):
        """Initialize OrderItem with ebook and quantity."""
        self.__ebook = ebook
        self.__quantity = quantity

    # Getters
    def get_ebook(self):
        return self.__ebook

    def get_quantity(self):
        return self.__quantity

    # Setters
    def set_quantity(self, quantity: int):
        self.__quantity = quantity

    def get_total_price(self):
        return self.__ebook.get_price() * self.__quantity

    def __str__(self):
        return f"OrderItem(ebook={self.__ebook.get_title()}, quantity={self.__quantity}, total_price={self.get_total_price()})"


class ShoppingCart:
    def __init__(self):
        """Initialize ShoppingCart with an empty list of order items."""
        self.__items = []

    def add_item(self, item: 'OrderItem'):
        self.__items.append(item)

    def remove_item(self, item: 'OrderItem'):
        self.__items.remove(item)

    def get_items(self):
        return self.__items

    def __str__(self):
        item_details = "\n".join([str(item) for item in self.__items])
        return f"ShoppingCart(items=\n{item_details})"
