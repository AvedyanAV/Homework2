import pytest
from src.class_product import Product


@pytest.fixture
def sample_product():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def another_product():
    return Product("iPhone 15 Pro", "512GB, Titanium", 200000.0, 3)


def test_product_initialization(sample_product):
    """Проверяем корректность инициализации продукта"""
    assert sample_product.name == "Samsung Galaxy S23 Ultra"
    assert sample_product.description == "256GB, Серый цвет, 200MP камера"
    assert sample_product.price == 180000.0
    assert sample_product.quantity == 5


def test_product_property(capsys, sample_product):
    """Проверяем защиту от установки недопустимой цены"""
    sample_product.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out


def test_product_addition(sample_product, another_product):
    """Тест сложения продуктов"""
    total = sample_product + another_product
    expected = (180000.0 * 5) + (200000.0 * 3)
    assert total == expected
