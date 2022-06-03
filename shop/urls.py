from xml.etree.ElementInclude import include
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.item_form),
    path('list/', views.item_list),
  
]