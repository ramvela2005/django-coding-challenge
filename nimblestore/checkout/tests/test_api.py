import os

import django
import pytest

# from checkout.models import Product
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nimblestore.settings")
django.setup()


@pytest.fixture
def api_client():
    return APIClient()


# TODO change to fit your product properties
@pytest.fixture
def create_product():
    pass
    # def _create_product(name, price, quantity):
    #     return Product.objects.create(name=name, price=price, quantity=quantity)
    # return _create_product


def dummy_test():
    assert 1 == 1


def dummy_failing():
    assert 1 == 2


def test_get_products(api_client, create_product):
    create_product(name="Test Product 1", price=10.00, quantity=100)
    create_product(name="Test Product 2", price=15.00, quantity=200)

    url = reverse("product-list")  # Adjust this to your actual URL name
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 2


def test_post_order(api_client, create_product):
    # product1 = create_product(name="Test Product 1", price=10.00, quantity=100)
    # product2 = create_product(name="Test Product 2", price=15.00, quantity=200)

    # TODO finish the test
    pass
