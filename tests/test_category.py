from src.category import Category


def test_category_init(first_cat):
    assert first_cat.name == "Смартфоны"
    assert (
        first_cat.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert first_cat.product == []
    assert Category.category_count == 1
    assert Category.product_count == 0
