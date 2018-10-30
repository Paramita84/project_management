# users/urls.py
from django.urls import path
from . import views,models

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('emp_details/', views.EmpDetails.as_view(), name='emp_details')]
