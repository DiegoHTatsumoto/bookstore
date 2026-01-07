import pytest
from order.serializers.order_serializers import OrderSerializer
from product import serializers
from product.models import Product
from django.contrib.auth.models import User
from order.models.order import Order

@pytest.mark.django_db
def test_order_serializer():
    user = User.objects.create_user(username="testuser")
    p1 = Product.objects.create(title="Produto 1", price=100, active=True)
    p2 = Product.objects.create(title="Produto 2", price=250, active=True)
    
    input_data = {
        "user": user.id,
        "products_id": [p1.id, p2.id]
    }

    serializer = OrderSerializer(data=input_data)
    assert serializer.is_valid(), serializer.errors
    
    order = serializer.save()
    
    output_data = OrderSerializer(order).data
    
    assert output_data["total"] == 350
    assert len(output_data["product"]) == 2
    assert output_data["product"][0]["title"] == "Produto 1"