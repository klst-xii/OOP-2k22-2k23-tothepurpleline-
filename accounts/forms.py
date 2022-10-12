from django import forms
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'placeholder': 'Email'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Password'
        }
    ))

    def clean(self):
        username = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)

        if not user or not user.is_active:
            raise forms.ValidationError("No entry")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        user = authenticate(username=username, password=password)

        return user

class RegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={
        "class": "form-control",
        "placeholder": "Email"
    }))
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "First Name"
    }))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Last Name"
    }))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Password"
    }))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Confirm Password"
    }))

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name',)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password2 != password1:
            raise forms.ValidationError("Password does not match")
        return password2

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()
        return user

