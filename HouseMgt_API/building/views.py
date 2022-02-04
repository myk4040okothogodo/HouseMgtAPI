from rest_framework import authentication, permissions, viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import  Building
from .serializer import BuildingSerializer



class DefaultsMixin(object):
    """Default settings for view authentication, permissions,
    filtering and pagination."""
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
         filters.OrderingFilter
            )
    
    
class BuildingViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating Buildings.""" 
    
    queryset = Building.objects.order_by('dateCommissioned')
    serializer_class = BuildingSerializer
    search_fields = ('name',)
    ordering_fields =('name',)
    
    
    
       
