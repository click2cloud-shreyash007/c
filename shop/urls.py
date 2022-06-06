from xml.etree.ElementInclude import include
from django.urls import path,include
from . import views

urlpatterns = [
    
    path('views/',views.item_form,name='item_insert'),  #get and post request for insert operation
    path('<int:id>/',views.item_form, name="item_update"),  #get and post request for update operation
    path('delete/<int:id>/',views.item_delete,name='item_delete'),
    path('list/', views.item_list,name='item_list'),  #get request to retieve list of items and display it
  
]