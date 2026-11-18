FROM python:3.11-slim 
# Use the official Python runtime image as your baseline kitchen

WORKDIR /app                  
# Establish an active working directory inside the 

COPY product_class.py inventory_class.py file_handling.py oop_inventory_manager.py PhysicalProduct.py DigitalProduct.py CanBeShipped.py Order.py OrderLine.py Supplier.py StudentDiscount.py products.csv ProductFactory.py product_loader.py PercentageDiscount.py NoDiscount. DiscountStrategy.py BulkDiscount.py ./
# Copy our local .py script into the container workspace

CMD [ "python", "oop_inventory_manager.py" ]
# Define the execution command to run when the container

  