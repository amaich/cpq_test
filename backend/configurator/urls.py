from django.urls import path
from .views import index, ProductListView, ProductGraph, ProductGraphView, CreateItemsView

app_name = "configurator"

urlpatterns = [
    path('', ProductListView.as_view(), name="product_list"),
    path('<int:product_id>/', ProductGraphView.as_view(), name="product_graph"),
    path('<int:product_id>/<int:attribute_id>/', ProductGraphView.as_view(), name="product_graph"),
    path('create_items/', CreateItemsView.as_view(), name="create_items")
]