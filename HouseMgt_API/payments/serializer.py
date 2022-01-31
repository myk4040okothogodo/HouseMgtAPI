from rest_framework import serializers
from .models impport Payments
from rest_framework.reverse import reverse
from ..HouseMgt_API.user.models import User



class PaymentSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField('get_links')
    payment_owner = serializer.SlugRelatedField(slug_field=User.USERNAME_FIELD, read_only=True)
    class Meta:
        model = Payment
        fields = ('id','building','room','tenant','amount_paid','receipt_no','links')
    def get_links(self,obj):
        request = self.context['request']
        return {'self': reverse('account-detail', kwargs={'pk':obj.pk}, request=request),}
