from src.category import Category

def test_category_init(first_cat):
    assert first_cat.name == "Смартфоны"
    assert first_cat.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    assert Category.category_count == 1
    assert Category.product_count == 0


def test_category(prod_one, prod_two):
    assert prod_one.name == "Смартфоны"
    assert (
        prod_one.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert prod_two.name == "Телевизоры"
    assert (
        prod_two.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )


    assert prod_one.category_count == 3
    assert prod_two.category_count == 3

    assert prod_one.product_count == 5
    assert prod_two.product_count == 5