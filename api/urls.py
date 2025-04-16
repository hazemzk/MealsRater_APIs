from django.urls import path, include
from rest_framework import routers
from .views import MealViewset, RatingViewset, UserViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('meals', MealViewset)
router.register('rating', RatingViewset)

urlpatterns =[
    path('', include(router.urls)),
]