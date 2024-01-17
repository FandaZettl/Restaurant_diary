from django.urls import path
from rest_framework import routers
from .views import RestaurantListCreateView, RestaurantDetailView, RestaurantViewSet

router = routers.DefaultRouter()
router.register(r'restaurants', RestaurantViewSet)

urlpatterns = router.urls
