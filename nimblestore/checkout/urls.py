from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("api", views.IndexView.as_view(), name="index"),
    path(
        "api/products/", views.ProductListView.as_view({"get": "list"}), name="products"
    ),
    path("api/order/", views.OrderView.as_view(), name="order"),
]
