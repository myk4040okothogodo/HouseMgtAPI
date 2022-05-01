from django.test import TestCase
from ..models import Payment
from  HouseMgt_API.user.models import User

class PaymentTest(TestCase):
    """Test module for the Payment model. """

    def setUp(self):
        Payment.objects.create(
            tenant =  User.objects.create(
                username = "Mr.Kevin Kimuzi",
                email = "kevin@gmail.com",
                phone_number = "+254717399590"
                ),
            amount_paid = 10000,
            receipt_no = 354,
            )
        Payment.objects.create(
            tenant = User.objects.create(
                username = "Mr.Karen Karanja",
                email = "karanja@gmail.com",
                phone_number = "+254799768597"
                ),
            amount_paid = 30000,
            receipt_no = 200,
            )

    
    def test_payment_owner(self):
        payment_receipt_no_200 = Payment.objects.get(receipt_no = 200)
        payment_receipt_no_354 = Payment.objects.get(receipt_no = 354)

        self.assertEqual(
            payment_receipt_no_200.tenant.username, "Mr.Karen Karanja"
            )
        self.assertEqual(
            payment_receipt_no_354.tenant.username, "Mr.Kevin Kimuzi"
            )
        
