def get_ordered_products_by_price(products):
   products.sort(key=lambda product: product.price, reverse=True)
   return products