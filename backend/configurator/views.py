from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .utils.graph import ItemGraph
from .utils.graph_utils import build_graph_with_attributes, build_tree
from .models import Item, Product, Attribute
import logging
import json

logging.getLogger(__name__)

def index(request):
    product = Product.objects.first()
    graph = ItemGraph(Item.objects.filter(product=product))

    graph = build_graph_with_attributes(graph=graph,
                                        start=Item.objects.get(name='Полочка'),
                                        attributes=Attribute.objects.all())

    return_str = ""
    builded_graph = graph.pretty_dfs(Item.objects.get(name='Полочка'))
    return_str += builded_graph

    return HttpResponse(return_str)


class ProductListView(ListView):
    model = Product
    template_name = 'configurator/product_list.html'
    context_object_name = 'products'


class ProductGraph(View):
    def get(self, request, product_id):
        product = Product.objects.get(id=product_id)
        graph = ItemGraph(Item.objects.filter(product=product))

        graph = build_graph_with_attributes(graph=graph,
                                            start=Item.objects.get(name='Полочка'),
                                            attributes=Attribute.objects.all())

        builded_graph = graph.pretty_dfs(Item.objects.get(name='Полочка'))
        builded_tree = build_tree(graph=graph,
                                  node=Item.objects.get(name='Полочка'),
                                  attributes=Attribute.objects.all())
        logging.info(f"----builded tree: {json.dumps(builded_tree, indent=2, ensure_ascii=False)}")

        return HttpResponse(builded_graph)


class ProductGraphView(View):
    def get(self, request, product_id, attribute_id=None):
        product = Product.objects.get(id=product_id)
        graph = ItemGraph(Item.objects.filter(product=product))

        attributes = Attribute.objects.filter(id__in=request.GET.getlist("view_type"))

        # TODO избавиться
        graph = build_graph_with_attributes(graph=graph,
                                            start=Item.objects.get(name='Полочка'),
                                            attributes=attributes)

        builded_tree = build_tree(graph=graph,
                                  node=Item.objects.get(name='Полочка'),
                                  attributes=attributes)

        logging.info(f"----builded tree: {json.dumps(builded_tree, indent=2, ensure_ascii=False)}")

        context = {
            "data": [builded_tree],
            "product_id": product_id,
            "available_attributes": Attribute.objects.all()
        }
        return render(request, "configurator/product_detail.html", context)


class CreateItemsView(APIView):
    def post(self, request):
        for item in request.data:
            parent = Item.objects.create(name=item,
                                         product_id=1)

        return Response(request.data, status=status.HTTP_200_OK)
