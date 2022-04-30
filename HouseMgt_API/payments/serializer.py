from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Payment
from rest_framework.reverse import reverse

User = get_user_model()



class PaymentSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField('get_links')
    payment_owner = serializers.SlugRelatedField(slug_field=User.USERNAME_FIELD, read_only=True)
    class Meta:
        model = Payment
        fields = ('id','tenant','amount_paid','receipt_no','date','payment_owner','links')
    def get_links(self,obj):
        request = self.context['request']
        links = {
                'self': reverse('payment-detail', 
                kwargs={'pk':obj.pk}, request=request),
                'tenant': None,
                'house':None,
                'payment_owner': None
                }
        """
        if obj.building_id:
            links['building'] = reverse('building-detail',
                kwargs ={'pk': obj.building_id}, request=request
                    )
        if obj.house_id:
            links['house'] = reverse('house-detail',
                kwargs = {'pk': obj.house_id}, request=request
                    )
        """            
        if obj.tenant_id:
            links['tenant'] = reverse('user-detail', kwargs={User.USERNAME_FIELD : obj.tenant_id}, request=request)
        return links    
