import unittest
from new_main import Product


def test_product(prod):
    assert prod.name == "Samsung Galaxy S23 Ultra"
    assert prod.description == "256GB, Серый цвет, 200MP камера"
    assert prod.price == 180000.0
    assert prod.quantity == 5


class TestProductPriceSetter(unittest.TestCase):

    def setUp(self):
        self.product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

    def test_set_positive_price(self):
        self.product.price = 210000.0
        self.assertEqual(self.product.price, 210000.0)


def test_prod_str(prod):
    assert str(prod) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
