import pytest
from src.class_product import Product, Smartphone, LawnGrass


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


def test_product_str(sample_product):
    """Проверка строкового представления продукта"""
    assert str(sample_product) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_smartphone_inheritance():
    """Тест наследования Smartphone от Product"""
    smartphone = Smartphone("Тест", "Тест", 100.0, 1, 90.0, "M1", 128, "Черный")

    assert isinstance(smartphone, Product)
    assert hasattr(smartphone, 'price')
    assert hasattr(smartphone, 'quantity')


def test_smartphone_add_type():
    """Тест сложения смартфонов одного типа"""
    phone1 = Smartphone("Phone1", "Desc1", 50000.0, 2, 90.0, "M1", 128, "Black")
    phone2 = Smartphone("Phone2", "Desc2", 60000.0, 1, 95.0, "M2", 256, "White")

    result = phone1 + phone2
    expected = (50000.0 * 2) + (60000.0 * 1)

    assert result == expected


def test_lawngrass_inheritance():
    """Тест наследования LawnGrass от Product"""
    grass = LawnGrass("Трава", "Описание", 100.0, 5, "РФ", "10 дней", "Зеленый")

    assert isinstance(grass, Product)
    assert hasattr(grass, 'price')
    assert hasattr(grass, 'quantity')


def test_lawngrass_add_type():
    """Тест сложения газонных трав одного типа"""
    grass1 = LawnGrass("Grass1", "Desc1", 1000.0, 10, "RU", "10 дней", "Green")
    grass2 = LawnGrass("Grass2", "Desc2", 1500.0, 5, "US", "12 дней", "Dark Green")

    result = grass1 + grass2
    expected = (1000.0 * 10) + (1500.0 * 5)

    assert result == expected
