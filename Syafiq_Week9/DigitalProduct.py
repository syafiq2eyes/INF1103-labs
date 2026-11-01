from product_class import Product

class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self.__download_size = download_size  # in MB

    def get_download_size(self):
        return self.__download_size

    def display_information(self):
        super().display_information()
        print(f"Download Size: {self.__download_size} MB")

    def get_fulfilment_info(self):
        return "This product is delivered digitally via download."

    def to_dict(self):
        """Return a dictionary representation of the DigitalProduct for JSON serialization."""
        data = super().to_dict()
        data["type"] = "digital"
        data["download_size"] = self.__download_size
        return data