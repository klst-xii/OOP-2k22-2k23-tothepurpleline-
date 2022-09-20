from django.contrib import admin
from django.urls import path

from .views import home_page, contact_page
from accounts.views import RegisterView

#

urlpatterns = [
    path('', home_page),
    path('contact/', contact_page),
    path('register/', RegisterView.as_view(), name='register'),
    path('admin/', admin.site.urls),
]
