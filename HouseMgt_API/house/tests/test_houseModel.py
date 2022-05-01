from  django.test import TestCase
from  ..models import House
from  HouseMgt_API.building.models import Building
from  HouseMgt_API.user.models import User

class HouseTest(TestCase):
    """ Test module for the Building model."""
    def setUp(self):
        House.objects.create(
            building = Building.objects.create(
                name  = "GREAT_WALL",
                owner = User.objects.create(
                    username = "Mr.Bill Kimati",
                    email = "kimati@gmail.com",
                    phone_number = "+245788417991",
                ),
                careTaker = User.objects.create(
                    username = "Mr.Perminus Makacha",
                    email = "makacha@gmail.com",
                    phone_number = "+254772456385",
                ),
                dateCommissioned = "2019-11-18",
                starsRating = 4,
                account_no  = 10078058,
            ),
            room_no = 23,
            floor_no = 2,
            tenant = User.objects.create(
                    username = "Mr.Peris Kerubo",
                    email = "kerubo@gmail.com",
                    phone_number = "+245071117001",
                ),
            occupied = True,
            )
        House.objects.create(
            building = Building.objects.create(
                name  = "SPRING_VALLEY",
                owner = User.objects.create(
                    username = "Mr.Indian Guy",
                    email = "patel@gmail.com",
                    phone_number = "+245722415610",
                ),
                careTaker = User.objects.create(
                    username = "Mr.Crispus Kamanda",
                    email = "kamanda@gmail.com",
                    phone_number = "+254766200615",
                ),
                dateCommissioned = "2012-04-10",
                starsRating = 3,
                account_no  = 22278060,
            ),
            room_no = 47,
            floor_no = 4,
            tenant = User.objects.create(
                    username = "Mr.Christine Stacy",
                    email = "stacy@gmail.com",
                    phone_number = "+245735337551",
                ),
            occupied = True,
            )

    def test_house_tenant(self):
        house_23 = House.objects.get(building = Building.objects.get(name="GREAT_WALL"   ), room_no = 23)
        house_47 = House.objects.get(building = Building.objects.get(name="SPRING_VALLEY"), room_no = 47)

        self.assertEqual(
            house_23.tenant.username, "Mr.Peris Kerubo"
            )
        self.assertEqual(
            house_47.tenant.username, "Mr.Christine Stacy"
            )
