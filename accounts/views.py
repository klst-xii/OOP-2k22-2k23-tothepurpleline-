from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import CreateView
from django.contrib.auth import login
from accounts.forms import RegisterForm, LoginForm


def login_page(request):
    form = LoginForm(request.POST or None)

    if request.POST and form.is_valid():
        user = form.login(request)
        print(user)
        if user:
            print(user)
            login(request, user)
            return redirect('home')
    context = {
        "form": form
    }
    return render(request, 'auth/login.html', context)

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'auth/register.html'
    success_url = '/'


