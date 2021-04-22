from homework11.task02.task02 import Order


def morning_discount(order):
    discount = 0.2
    return order.price - order.price * discount


def daily_discount(order):
    discount = 0
    return order.price - order.price * discount


def elder_discount(order):
    discount = 0.5
    return order.price - order.price * discount


def test_order_class_with_different_discounts():
    order_1 = Order(100, morning_discount)
    order_2 = Order(100, daily_discount)
    order_3 = Order(100, elder_discount)
    assert order_1.final_price() == 80.0
    assert order_2.final_price() == 100.0
    assert order_3.final_price() == 50.0
