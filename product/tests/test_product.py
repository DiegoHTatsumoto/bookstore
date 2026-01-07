import pytest
from product.models.product import Product

@pytest.mark.django_db
def test_create_product():
    product = Product.objects.create(
        title="Test Product",
        description="This is a test product.",
        price=1000,
        active=True,
    )
    assert product.title == "Test Product"
    assert product.description == "This is a test product."
    assert product.price == 1000
    assert product.active is True
    assert product.category.count() == 0