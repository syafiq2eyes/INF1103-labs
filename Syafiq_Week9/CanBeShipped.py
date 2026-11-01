from product_class import Product
from abc import ABC, abstractmethod

class CanBeShipped(Product, ABC):
    @abstractmethod
    def calculate_shipping_cost(self):
        """Return the shipping cost for this item."""
        pass  # No implementation
