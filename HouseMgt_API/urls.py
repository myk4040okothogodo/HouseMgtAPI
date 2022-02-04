from rest_framework.routers import DefaultRouter
from .building.view import BuildingViewSet
from .payment.view import PaymentViewSet
from .user.view import UserViewSet
from .house.view import HouseViewSet

router = DefaultRouter()

router.register(r'houses' , HouseViewSet)
router.register(r'users', UserViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'buildings', BuildingViewSet)


