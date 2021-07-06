from django.urls import re_path
from Register import views

urlpatterns = [    
    re_path(r'get/(?P<id>\d+)/$', views.UsersList.as_view()),
    re_path(r'^', views.RegisterUser.as_view()),
]