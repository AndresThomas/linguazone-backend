from django.urls import re_path
from groups import views

urlpatterns = [    
    re_path(r'get/(?P<id>\d+)/$', views.GroupsList.as_view()),
    re_path(r'^', views.Registergroup.as_view()),
]