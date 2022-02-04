from django.contrib.auth import get_user_model
from rest_framework import authentication, permissions, viewsets
from .model import Payment
from .serializer import PaymentSerializer


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
    
    
class _PaymentViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpooint for listing and creating Payments."""
    queryset = Payment.objects.order_by('date')
    sserializer_class = PaymentSerializer
    
