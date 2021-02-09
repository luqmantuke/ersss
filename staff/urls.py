from django.urls import path
from .views import staff_list, staff_detail

urlpatterns = [
    path('staff', staff_list, name="staff_list"),
    path('staff/<slug:slug>/', staff_detail, name="staff_detail")
]