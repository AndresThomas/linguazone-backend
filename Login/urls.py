from django.urls import re_path

from Login.views import CustomAuthToken

urlpatterns = [
    
    re_path(r'^', CustomAuthToken.as_view(),name='login'),

]