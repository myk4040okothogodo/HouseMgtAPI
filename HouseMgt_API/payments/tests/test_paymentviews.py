from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient
from ..views import PaymentViewSet

class TestHouse(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.factory = APIRequestFactory()
        self.view  = PaymentViewSet.as_view({'get': 'list'})
        self.uri = '/payments/'
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

    def test_payments(self):
        request = self.factory.get(self.uri,
            HTTP_AUTHORIZATION = 'Token {}'.format(self.token.key)
                                   )
        request.user = self.user
        response = self.view(request)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code)
                         )

    def test_payments2(self):
        response = self.client.get(self.uri)
        self.assertEqual(response.status_code, 200,
                'Expected Response Code 200, received {0} instead.'
                .format(response.status_code)
                )


    def test_create(self):
        self.client.login(username="test", password="test")
        params = {
                'tenant' : {
                    'username' :  'Mr.Bill Kimati',
                    'email' : 'kimati@gmail.com',
                    'phone_number' : '+245788417991',
                    },
                'amount_paid': '10000',
                'receipt_no': '546627',
                'date' : '2019-11-18',
        response = self.client.post(self.uri, params, format="json")
        self.assertEqual(response.status_code, 201,
                'Expected Response Code 201, received {0} instead.'
                .format(response.status_code)
                )
