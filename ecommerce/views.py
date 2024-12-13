from rest_framework import mixins, permissions, viewsets
from rest_framework.response import Response

from ecommerce.models import Order, OrderItems
from ecommerce.serializers import OrderItemsSerializer, OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderItemsViewSet(viewsets.ModelViewSet):
    queryset = OrderItems.objects.all()
    serializer_class = OrderItemsSerializer

