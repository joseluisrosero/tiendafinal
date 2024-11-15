from django.urls import path, include
from rest_framework import routers
from home2.models import *
from webservices.views import *

router = routers.DefaultRouter()
router.register(r'producto' , producto_viewset)
router.register(r'marca' , marca_viewset)
router.register(r'categoria' , categoria_viewset)

urlpatterns = [
    
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]


