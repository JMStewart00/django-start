from django.urls import path, include
from rest_framework import routers
from .views import PizzaToppingViewSet, PizzaTypeViewSet

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register(r'pizza-toppings', PizzaToppingViewSet)
router.register(r'pizza-types', PizzaTypeViewSet)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]
