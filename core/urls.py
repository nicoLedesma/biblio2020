from django.urls import path,include
from core.views import HomeView, current_datetime, current_datetime1,current_datetime2
    #hello, current_datetime


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    #path('hello/'),
    path('time/', current_datetime),
    path('time1/', current_datetime1),
    path('time2/', current_datetime2),

]