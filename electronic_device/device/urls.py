from django.urls import path,include
from .views import device_detail,device_list
from .import views 
urlpatterns = [

    path('',views.device_list),
    path('device/<int:id>',views.device_detail),
]
