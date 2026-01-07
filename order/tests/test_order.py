import pytest
from order.models.order import Order
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_create_order():
    user = User.objects.create_user(username="testuser")
    order = Order.objects.create(
        user=user
    )

    assert order.user.username == "testuser"
    assert order.product.count() == 0