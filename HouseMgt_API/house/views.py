from rest_framework import viewsets,permissions,authentication, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import House
from .serializer import HouseSerializer
# Create your views here.


class DefaultsMixin(object):
    """Default settings for view authentication, permissions, filtering and pagination."""
    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
            )
    permission_classes = (
        permissions.IsAuthenticated,
            )
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
            )



class HouseViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating Houses."""
    queryset = House.objects.order_by('room_no')
    serializer_class = HouseSerializer
    search_fields = ('building', 'tenant','occupied')
    ordering_fields = ('occupied','room_no','building')
