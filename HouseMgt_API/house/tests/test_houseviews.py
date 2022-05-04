"""
DRF provides a few important classes which make testing APIs simpler,

1. APIRequestFactory : this class is similar to Django's RequestFactory. It allows
one to create any http method,which you can then pass to any view method and compare respponse

2. APIClient : similar to Djangos Client. One can GET or POST a URL, and test responses

3.APITestCase : similar to Djangos' TestCase, tests will sublass this

"""

#Django Rest Framework has a class called APIRequestFactory which extends the standard Django RequestFactory
#This class contains almost all of the http verbs like .get() .post(), .put() .patch() et all

from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient
from ..views import HouseViewSet

class TestHouse(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.factory = APIRequestFactory()
        self.view  = HouseViewSet.as_view({'get': 'list'})
        self.uri = '/houses/'
        self.user = self.setup_user()
        self.token = Token.objects.create(user = self.user)
        self.token.save()

    @staticmethod
    def setup_user():
        User = get_user_model()
        return User.objects.create_user(
            username= 'test',
            email = 'testuser@test.com',
            password = 'test',
            phone_number = '+25470000000'
        )

    def test_houses(self):
        request = self.factory.get(self.uri,
            HTTP_AUTHORIZATION = 'Token {}'.format(self.token.key)
                                   )
        request.user = self.user
        response = self.view(request)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code)
                         )

    def test_houses2(self):
        response = self.client.get(self.uri)
        self.assertEqual(response.status_code, 200,
                'Expected Response Code 200, received {0} instead.'
                .format(response.status_code)
                )


    def test_create(self):
        self.client.login(username="test", password="test")
        params = {
                'name'  : "GREAT_WALL",
                'owner' : {
                    'username' :  'Mr.Bill Kimati',
                    'email' : 'kimati@gmail.com',
                    'phone_number' : '+245788417991',
                    },
                'careTaker' : {
                    'username' : 'Mr.Perminus Makacha',
                    'email' :  'makacha@gmail.com',
                    'phone_number' : '+254772456385',
                    },
                'dateCommissioned' : '2019-11-18',
                'starsRating' : '4',
                'account_no'  : '10078058',     
                }
        response = self.client.post(self.uri, params, format="json")
        self.assertEqual(response.status_code, 201,
                'Expected Response Code 201, received {0} instead.'
                .format(response.status_code)
                )

