import pytest
from product.models.product import Category
from product.serializers.product_serializer import ProductSerializer

@pytest.mark.django_db
def test_product_serializer_full_fields():
    category = Category.objects.create(title="Hardware")
    
    data = {
        "title": "Placa de Video",
        "description": "RTX 3060",
        "price": 10000,
        "active": True,
        "categories_id": [category.id]
    }

    serializer = ProductSerializer(data=data)
    assert serializer.is_valid(), serializer.errors
    product = serializer.save()
    output_data = serializer.data
    assert output_data["id"] == product.id
    assert len(output_data["category"]) == 1
    assert output_data["category"][0]["title"] == "Hardware"
    assert "categories_id" not in output_data
    assert output_data["title"] == data["title"]
    assert output_data["price"] == data["price"]