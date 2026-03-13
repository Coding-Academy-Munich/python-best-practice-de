class OrderLine:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.product.price * self.quantity


def make_order_lines():
    return [
        OrderLine("apple", 10, 1.0),
        OrderLine("banana", 5, 0.5),
    ]
