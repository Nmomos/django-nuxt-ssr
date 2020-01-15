from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WaterPlantsViewSet

router = DefaultRouter()
router.register(r"waterplants", WaterPlantsViewSet)

urlpatterns = [path("", include(router.urls))]
