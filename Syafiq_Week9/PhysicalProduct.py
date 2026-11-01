from product_class import Product
from CanBeShipped import CanBeShipped

class PhysicalProduct(Product):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight  # Weight in kilograms

    def get_weight(self):
        return self.__weight

    def display_information(self):
        super().display_information()
        print(f"Weight: {self.__weight} kg")

    def get_fulfilment_info(self):
        return "This product requires physical shipping."

    def calculate_shipping_cost(self):
        return 5.00 + 2.00 * self.__weight  # Base cost + cost per kg

    def to_dict(self):
        """Return a dictionary representation of the PhysicalProduct for JSON serialization."""
        data = super().to_dict()
        data["type"] = "physical"
        data["weight"] = self.__weight
        return data