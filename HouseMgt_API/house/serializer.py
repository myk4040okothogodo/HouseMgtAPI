from rest_framework import serializers
from .models import House
from rest_framework.reverse import reverse
from django.contrib.auth import get_user_model

User = get_user_model()



class HouseSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField('get_links')
    assigned = serializers.SlugRelatedField(slug_field=User.USERNAME_FIELD, required=False)
    house_owner = serializer.SlugRelatedField(slug_field=User.USERNAME_FIELD, read_only=True)
    class Meta:
        model = House
        fields = ('id','building','room_no','floor_no','occupied','tenant','assigned','links')
    def get_links(self,obj):
        request = self.context['request']
        return {'self': reverse('house-detail', kwargs={'pk':obj.pk}, request=request),}
