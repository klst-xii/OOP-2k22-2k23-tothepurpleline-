from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import CreateView
from django.contrib.auth import login
from accounts.forms import RegisterForm, LoginForm
from django.views.generic.edit import DeleteView
from .forms import User
from django.urls import reverse_lazy


def login_page(request):
    form = LoginForm(request.POST or None)

    if request.POST and form.is_valid():
        user = form.login(request)
        print(user)
        if user:
            print(user)
            login(request, user)
            return redirect('post-list')
    context = {
        "form": form
    }
    return render(request, 'auth/login.html', context)


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'auth/register.html'
    success_url = '/'


class CustomUserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('register')

# def user_delete(request, pk):
#     user_pk = request.user.pk
#     auth_logout(request)
#     User = get_user_model()
#     User.objects.filter(pk=user_pk).delete()
#     return render('register')