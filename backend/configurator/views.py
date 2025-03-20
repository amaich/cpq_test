from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


from .utils.graph import ItemGraph
from .models import Item, Product
import logging

logging.getLogger(__name__)

def index(request):


    product = Product.objects.first()

    graph = ItemGraph(Item.objects.filter(product=product))

    logging.info(graph.nodes)

    return_str = ""

    builded_graph = graph.pretty_dfs(Item.objects.get(name='Полочка'))
    logging.info(f"----------{builded_graph}")
    return_str += "<p>--------</p>"
    return_str += builded_graph
    return HttpResponse(return_str)


class CreateItemView(APIView):
    def post(self, request):

        return Response