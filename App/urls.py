from django.urls import path
from .views import GetHomePage , GetAboutPage

urlpatterns = [
    path('/home', GetHomePage , name="home"  ),
    path('/about', GetAboutPage , name="about" )
]
