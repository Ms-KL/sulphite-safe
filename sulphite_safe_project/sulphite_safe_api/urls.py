from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('beverages', views.BeverageViewSet)
router.register('sulphite_statuses', views.SulphiteStatusViewSet)
router.register('beverage_sulphite_statuses', views.BeverageSulphiteStatusViewSet)
router.register('user_beverage_sulphite_statuses', views.UserBeverageSulphiteStatusViewSet)

urlpatterns = [
    path('', include(router.urls)),

]

