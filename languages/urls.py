from django.urls import re_path
from languages import views

urlpatterns = [    
    re_path(r'get/(?P<id>\d+)/$', views.LanguageList.as_view()),
    re_path(r'^', views.RegisterLanguage.as_view()),
]