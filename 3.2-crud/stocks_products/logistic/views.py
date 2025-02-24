from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from django.http import HttpResponse
from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer

def index(request):
    return HttpResponse("Hello cicd v2")

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # при необходимости добавьте параметры фильтрации
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description']


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    # при необходимости добавьте параметры фильтрации
    filter_backends = [SearchFilter]
    search_fields = ['products__title', 'products__description']
