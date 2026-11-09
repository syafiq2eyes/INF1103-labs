from abc import ABC, abstractmethod
from Supplier import Supplier

class Product(ABC):
    def __init__(self, product_id: str, name: str, price: float, stock:int, supplier: Supplier) -> None:
        self.__product_id: str = product_id
        self.__name: str = name
        self.__price: float = price
        self.__stock: int = stock
        self.__supplier: Supplier = supplier

    def get_product_id(self) -> str:
        return self.__product_id

    def get_name(self) -> str:
        return self.__name

    def get_price(self) -> float:
        return self.__price

    def get_stock(self) -> int:
        return self.__stock

    def get_supplier(self) -> Supplier:
        return self.__supplier

    def to_dict(self) -> dict[str, str | float | int]:
        return {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock,
            "supplier": self.__supplier.to_dict()
        }
    
    def display_information(self) -> None:
        print(f"{self.__product_id} | {self.__name} | ${self.__price:.2f} | {self.__stock} in stock")

    def update_stock(self, quantity: int) -> None:
        if quantity < 0:
            raise ValueError("Stock cannot be negative.")
        self.__stock = quantity


    @abstractmethod
    def get_fulfilment_info(self)-> str:
        """Return specific fulfilment information for the product."""
        pass                              # No implementation
