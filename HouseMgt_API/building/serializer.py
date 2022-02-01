from rest_framework import serializers
from .models impport Building
from rest_framework.reverse import reverse
from ..user.models import User



class BuildingSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField('get_links')
    building_owner = serializer.SlugRelatedField(slug_field=User.USERNAME_FIELD, read_only=True)
    class Meta:
        model = Building
        fields = ('id','name','owner','caretaker','houses','starsRating','account_no')
    def get_links(self,obj):
        request = self.context['request']
        return {'self': reverse('account-detail', kwargs={'pk':obj.pk}, request=request),}
