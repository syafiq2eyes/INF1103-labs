from product_class import Product
from CanBeShipped import CanBeShipped
from Supplier import Supplier

class PhysicalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier, weight: float) -> None:
        super().__init__(product_id, name, price, stock, supplier)
        self.__weight: float = weight  # Weight in kilograms

    def get_weight(self) -> float:
        return self.__weight

    def display_information(self) -> None:
        super().display_information()
        print(f"Weight: {self.__weight} kg")

    def get_fulfilment_info(self) -> str:
        return "This product requires physical shipping."

    def calculate_shipping_cost(self) -> float:
        return 5.00 + 2.00 * self.__weight  # Base cost + cost per kg

    def to_dict(self) -> dict[str, str | float | int]:
        """Return a dictionary representation of the PhysicalProduct for JSON serialization."""
        data = super().to_dict()
        data["type"] = "physical"
        data["weight"] = self.__weight
        return data