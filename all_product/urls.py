from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

routers = DefaultRouter()
routers.register("",views.BennerViewset)



urlpatterns = [
  path("benner/", include(routers.urls)), 
  path("text/", views.TextViewApi.as_view())  
]

