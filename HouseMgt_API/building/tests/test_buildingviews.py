import json
from rest_framework import status
from django.test import TestCase , Client
from django.urls import reverse
from ..models import Building
from ..serializer import BuildingSerializer
from HouseMgt_API.user.models import User
#initialize the APIClient app
from ..views import BuildingViewSet


client = Client()

class GetAllBuildingsTest(TestCase):
    """ Test module for GET all building API."""
    def setUp(self):
        self.RED_CLASSIC = Building.objects.create(
            name  = "RED_CLASSIC",
            owner = User.objects.create(
                username = "Mr.Asumo Otieno",
                email = "otieno@gmail.com",
                phone_number = "+245755247920",
                ),
            careTaker = User.objects.create(
                username = "Mr.Travis Mwambua",
                email = "mwambua@gmail.com",
                phone_number = "+254790456187",
                ),
            dateCommissioned = "2018-03-21",
            starsRating = 3,
            account_no  = 83578032,
            )
        self.BEMA_APARTMENT = Building.objects.create(
            name  = "BEMA_APARTMENT",
            owner = User.objects.create(
                username = "Mr.Erick Kivuli",
                email = "kivuli@gmail.com",
                phone_number = "+245733107911",
                ),
            careTaker = User.objects.create(
                username = "Mr.Dennis Otiva",
                email = "otiva@gmail.com",
                phone_number = "+254711456888",
                ),
            dateCommissioned = "2018-03-21",
            starsRating = 3,
            account_no  = 83578032,
            )
        self.GREAT_WALL = Building.objects.create(
            name  = "GREAT_WALL",
            owner = User.objects.create(
                username = "Mr.Kipchirchir Kiptum",
                email = "kiptum@gmail.com",
                phone_number = "+245700247900",
                ),
            careTaker = User.objects.create(
                username = "Mr.Elvis Mwanza",
                email = "mwanza@gmail.com",
                phone_number = "+254790456187",
                ),
            dateCommissioned = "2018-03-21",
            starsRating = 3,
            account_no  = 83578032,
            )
    def test_get_all_buildings(self):
        #get API response
        response = client.get(BuildingViewSet)

        buildings = Building.objects.all()
        serializer = BuildingSerializer(buildings, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code , status.HTTP_200_OK)

    def test_get_valid_single_building(self):
        response = client.get(BuildingViewSet, kwargs={'pk': self.GREAT_WALL.pk})
        building = Building.objects.get(pk = self.GREAT_WALL.pk)
        serializer = BuildingSerializer(building)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_get_invalid_single_building(self):
        response = client.get(BuildingViewSet, kwargs={'pk': 30})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewBuilding(TestCase):
    """Test module for insserting a new building"""
    def setUp(self):
        self.valid_payload = {
            'name'  : 'RED_CLASSIC',
            'owner' : {
                'username' : 'Mr.Patrick butito',
                'email' : 'butito@gmail.com',
                'phone_number' : "+245788247100",
                },
            'careTaker' :  {
                'username' : 'Mr.Travis Mwambua',
                'email' : 'mwambua@gmail.com',
                'phone_number': '+254790456187',
                },
            'dateCommissioned' : '2018-03-21',
            'starsRating' : '3',
            'account_no' :'83578032',    
            }
        self.valid_payload = {
            'name'  : 'GREAT_WALL',
            'owner' : {
                'username' : 'Mr.Erick Kimuli',
                'email' : 'kimuli@gmail.com',
                'phone_number' : "+245788247100",
                },
            'careTaker' : {
                'username' : 'Mr.Travis Mwambua',
                'email' : 'mwambua@gmail.com',
                'phone_number': '+254790456187',
                },
            'dateCommissioned' : '2018-03-21',
            'starsRating' : '3',
            'account_no' :'83578032',    
            }
    def test_create_valid_building(self):
        response = client.post(
            BuildingViewSet,
            data = json.dumps(self.valid_payload),
            content_type = 'application/json'
            )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    def test_create_invalid_building(self):
        response = client.post(
            BuildingViewSet,
            data = json.dumps(self.invalid_payload),
            content_type = 'application/json'
            )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class DeleteingleBuildingTest(TestCase):
    """ Test module for deleteing an existing Building record."""
    def setUp(self):
        self.RED_CLASSIC = Building.objects.create(
            name  = "RED_CLASSIC",
            owner = User.objects.create(
                username = "Mr.Asumo Otieno",
                email = "otieno@gmail.com",
                phone_number = "+245755247920",
                ),
            careTaker = User.objects.create(
                username = "Mr.Travis Mwambua",
                email = "mwambua@gmail.com",
                phone_number = "+254790456187",
                ),
            dateCommissioned = "2018-03-21",
            starsRating = 3,
            account_no  = 83578032,
            )
        self.BEMA_APARTMENT = Building.objects.create(
            name  = "BEMA_APARTMENT",
            owner = User.objects.create(
                username = "Mr.Erick Kivuli",
                email = "kivuli@gmail.com",
                phone_number = "+245733107911",
                ),
            careTaker = User.objects.create(
                username = "Mr.Dennis Otiva",
                email = "otiva@gmail.com",
                phone_number = "+254711456888",
                ),
            dateCommissioned = "2018-03-21",
            starsRating = 3,
            account_no  = 83578032,
        )
    def test_valid_delete_building(self):
            response = client.delete(
                BuildingViewSet, kwargs={'pk': self.BEMA_APARTMENT.pk})
            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    def test_invalid_delete_building(self):
            response = client.delete(
                BuildingViewSet, kwargs={'pk' : 30})
            self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
