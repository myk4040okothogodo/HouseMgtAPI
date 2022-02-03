from rest_framework import viewsets,permissions,authentication
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



class HouseViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating Houses."""
    queryset = House.objects.order_by('building')
    serializer_class = HouseSerializer
