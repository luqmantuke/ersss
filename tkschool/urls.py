from django.urls import path
from .views import home, aboutus


urlpatterns = [
    path('', home, name="home"),
    path('aboutus/', aboutus, name="aboutus"),
]
