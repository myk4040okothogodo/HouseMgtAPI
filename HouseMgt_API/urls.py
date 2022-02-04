from rest_framework.routers import DefaultRouter
from .building.views import  BuildingViewSet
from .payments.views import PaymentViewSet
from .user.views import UserViewSet
from .house.views import HouseViewSet

router = DefaultRouter()

router.register(r'houses' , HouseViewSet)
router.register(r'users', UserViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'buildings', BuildingViewSet)


