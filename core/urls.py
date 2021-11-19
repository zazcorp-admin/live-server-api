from django.urls import path, include
from . import views 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('item', views.ItemViewset, basename='item')

urlpatterns = [
	# path('', views.index, name='home')
	path('', include(router.urls))
]