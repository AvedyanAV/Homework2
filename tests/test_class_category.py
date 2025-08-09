import pytest
from src.class_product import Product
from src.class_category import Category

@pytest.fixture
def sample_products():
    return [
        Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
        Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
        Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)  # Дубликат по имени
    ]


@pytest.fixture
def sample_category(sample_products):
    return Category("Электроника", "Техника", sample_products)


def test_category_initialization(sample_category, sample_products):
    """Проверяем корректность инициализации категории"""
    assert sample_category.name == "Электроника"
    assert sample_category.description == "Техника"
    assert len(sample_products) == 3


def test_total_categories_count(sample_category):
    """Проверяем подсчет количества категорий"""
    assert Category.category_count >= 1  # Как минимум наша категория

