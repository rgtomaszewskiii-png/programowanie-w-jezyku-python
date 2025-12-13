def calculate_total_price(products):
    total = 0
    for product in products:
        total += product.price
    return total

import utils


class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f"Product(name={self.name}, price={self.price})"

    import utils
    from product import Product

    class Order:
        def __init__(self, products: list[Product]):
            self.products = products
            self.total_price = utils.calculate_total_price(products)

        def __str__(self) -> str:
            return f"Order(total_price={self.total_price})"

        from product import Product
        from order import Order

        def main():
            product1 = Product("Laptop", 3000)
            product2 = Product("Mouse", 150)

            order = Order([product1, product2])
            print(order)

        if __name__ == "__main__":
            main()