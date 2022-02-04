from rest_framework import serializers
from .models import Building
from rest_framework.reverse import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class BuildingSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField('get_links')
    assigned_caretaker = serializers.SlugRelatedField(slug_field=User.USERNAME_FIELD, read_only=True)
    class Meta:
        model = Building
        fields = ('id','name','owner','careTaker','starsRating','dateCommissioned','assigned_caretaker','account_no','links')
    def get_links(self,obj):
        request = self.context['request']
        links = {
                'self': reverse('building-detail',
                kwargs={'pk':obj.pk}, request=request),
            'houses':None,
            'careTaker': None,
            'owner': None,
        }
           
        if obj.careTaker_id:
            links['careTaker'] = reverse('user-detail',
                kwargs ={User.USERNAME_FIELD: obj.careTaker}, request=request
                    )

        if obj.owner_id:
            links['owner'] = reverse('user-detail',
                kwargs = {User.USERNAME_FIELD: obj.owner}, request=request
                    )
        return links    
