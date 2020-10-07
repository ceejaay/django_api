# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'heros', views.HeroViewSet)
router.register(r'villians', views.VillianViewSet)

urlpatterns = [
        path('', include(router.urls)),
        path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
        path('villians/', include(router.urls)),
        ]
