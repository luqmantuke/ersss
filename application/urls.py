from django.urls import path
from .views import olevel, alevel, applications


urlpatterns = [
    path('olevelapplications/', olevel, name="olevelapplication"),
    path('alevelapplications/', alevel, name="alevelapplication"),
    path('applications/', applications, name="applications"),

]