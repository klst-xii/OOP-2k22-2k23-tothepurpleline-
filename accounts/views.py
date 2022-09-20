from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView

from accounts.forms import RegisterForm


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'auth/register.html'
    success_url = '/'


