from django.shortcuts import render
from django.http import HttpResponse
from .services.graph import ItemGraph
from .models import Item, Product
import logging

logging.getLogger(__name__)

def index(request):
    graph = ItemGraph()

    product = Product.objects.first()

    for item in Item.objects.filter(product=product):
        graph.add_node(item.name)
        for sub_item in item.items.all():
            graph.add_edge(item.name, sub_item.name)

    graph.dfs("Полочка")

    return HttpResponse("daji")