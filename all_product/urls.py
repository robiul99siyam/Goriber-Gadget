from django.urls import path
from . import views



urlpatterns = [
  path("",views.TextViewApi.as_view())
]
