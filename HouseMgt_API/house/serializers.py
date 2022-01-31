from rest_framework import serializers
from .models import House
from rest_framework.reverse import reverse
from ..HouseMgt_API.user.models import User



class HouseSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField('get_links')
    house_owner = serializer.SlugRelatedField(slug_field=User.USERNAME_FIELD, read_only=True)
    class Meta:
        model = House
        fields = ('id','building','room_no','floor_no','tenant','links')
    def get_links(self,obj):
        request = self.context['request']
        return {'self': reverse('account-detail', kwargs={'pk':obj.pk}, request=request),}i
