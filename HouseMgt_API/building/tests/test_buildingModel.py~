from django.test import TestCase
from ..models import Building
from  HouseMgt_API.user.models import User


class BuildingTest(TestCase):
    """ Test module for the Builing model."""

    def setUp(self):
        Building.objects.create(
            name  = "RED_CLASSIC",
            owner = User.objects.create(
                username = "Mr.Erick Otieno",
                email = "erick@gmail.com",
                phone_number = "+245700247900",
                ),
            careTaker = User.objects.create(
                username = "Mr.Dennis Mwambua",
                email = "mwambua@gmail.com",
                phone_number = "+254790456187",
                ),
            dateCommissioned = "2018-03-21",
            starsRating = 3,
            account_no  = 83578032,
            )
        Building.objects.create(
            name  = "BEMA_APARTMENTS",
            owner = User.objects.create(
                username = "Mr.Kitili Kinjeti",
                email = "kinjeti@gmail.com",
                phone_number = "+245739157940",
                ),
            careTaker = User.objects.create(
                username = "Mr.Justus kariuki",
                email = "kariuki@gmail.com",
                phone_number = "+254713565257",
                ),
            dateCommissioned = "2014-10-01",
            starsRating = 2,
            account_no  = 83578032,
            )

    def   test_building_owner(self):
        building_red = Building.objects.get(name = "RED_CLASSIC")
        building_bema = Building.objects.get(name= "BEMA_APARTMENTS")
        self.assertEqual(
            building_red.owner.username, "Mr.Erick Otieno"
            )
        self.assertEqual(
            building_bema.owner.username, "Mr.Kitili Kinjeti"    
            )
