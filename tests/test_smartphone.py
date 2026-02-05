import pytest


def test_prod_init(add_prod1):
    assert add_prod1.name == "Iphone 15"
    assert add_prod1.description == "512GB, Gray space"
    assert add_prod1.price == 210000.0
    assert add_prod1.efficiency == 98.2
    assert add_prod1.model == "15"
    assert add_prod1.memory == 512
    assert add_prod1.color == "Gray space"


def test_prod_add(add_prod1):
    with pytest.raises(TypeError):
        add_prod1 + 1
