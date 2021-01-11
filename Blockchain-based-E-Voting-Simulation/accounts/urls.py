from django.urls import include, path
from . import views


urlpatterns = [
    path('',views.signup,name='signup'),
    path('me/',views.login,name='login'),
]
