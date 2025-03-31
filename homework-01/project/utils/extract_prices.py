from models.product import Product

def extract_prices(products):
    return [product.price for product in products]
