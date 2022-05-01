from django.test import TestCase
from ..models import User



class UserTest(TestCase):
    """Test module for the user model."""
    def setUp(self):
        User.objects.create(
             username = "Mr.Kimani Ngunjiri",
             email = "ngunjiri@gmail.com",
             phone_number = "+245766119000",
        )

        User.objects.create(
             username = "Mr.Patrick Batizo",
             email = "batizo@gmail.com",
             phone_number = "+245744307911",
            
        )

    def test_user_email(self):
        user_kimani = User.objects.get(username="Mr.Kimani Ngunjiri")
        user_patrick = User.objects.get(username="Mr.Patrick Batizo")

        self.assertEqual(
            user_kimani.email, "ngunjiri@gmail.com"
            )

        self.assertEqual(
            user_patrick.email, "batizo@gmail.com"
            )
