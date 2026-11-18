from DigitalProduct import DigitalProduct
from PhysicalProduct import PhysicalProduct
from product_class import Product
from Supplier import Supplier

class ProductFactory:
    @staticmethod
    def create(product_type: str, product_id: str, name: str, price: float,
               stock_quantity: int, supplier: Supplier, extra:float) -> Product:
        if product_type == "physical":
            return PhysicalProduct(product_id, name, price, stock_quantity, supplier, extra)
        elif product_type == "digital":
            return DigitalProduct(product_id, name, price, stock_quantity, supplier, extra)
        else:
            raise ValueError(f"Unknown product type: {product_type}")
