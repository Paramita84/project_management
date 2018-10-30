from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic
from .models import CustomUser

from .forms import CustomUserCreationForm

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('emp_details')
    template_name = 'signup.html'


class EmpDetails(generic.ListView):
    model = CustomUser
    template_name = 'emp_details.html'

