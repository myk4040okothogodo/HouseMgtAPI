from rest_framework import serializers
from .models import Building
from rest_framework.reverse import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class BuildingSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField('get_links')
    building_owner = serializers.SlugRelatedField(slug_field=User.USERNAME_FIELD, read_only=True)
    class Meta:
        model = Building
        fields = ('id','name','owner','careTaker','starsRating','dateCommissioned','account_no')
    def get_links(self,obj):
        request = self.context['request']
        return {'self': reverse('building-detail', kwargs={'pk':obj.pk}, request=request),}
