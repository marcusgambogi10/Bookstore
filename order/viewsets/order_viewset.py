from order.models import Order
from order.serializers import OrderSerializer

from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class OrderViewSets(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all().order_by('id')