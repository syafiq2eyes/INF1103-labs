from product_class import Product

class OrderLine:
    def __init__(self, product: Product, quantity: int):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than Zero.")
        self.__product: Product = product
        self.__quantity: int = quantity

    def get_product(self) -> Product:
        return self.__product

    def get_quantity(self) -> int:
        return self.__quantity

    def calculate_subtotal(self) -> float:
        return self.__product.get_price() * self.__quantity

    def display_information(self) -> None:
        product = self.__product
        print(
            f"{product.get_name()} x {self.__quantity} @ ${product.get_price():.2f}" 
            f"= ${self.calculate_subtotal():.2f}"
        )
        