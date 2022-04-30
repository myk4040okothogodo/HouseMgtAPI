from django.contrib.auth import get_user_model
from rest_framework import authentication, permissions, viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Payment
from .serializer import PaymentSerializer

from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope


class DefaultsMixin(object):
    """Default settings for view authentication, permissions,
    filtering and pagination."""
    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )
    permission_classes = (
        permissions.IsAuthenticated,
        #TokenHasReadWriteScope
    )
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,

            )
    
    
class PaymentViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating Payments."""
    
    queryset = Payment.objects.order_by('date')
    serializer_class = PaymentSerializer
    search_fields = ('tenant','receipt_no','date')
    ordering_fields =('date','receipt_no','tenant')
