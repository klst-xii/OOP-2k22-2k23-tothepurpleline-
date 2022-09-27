from django.contrib import admin
from django.urls import path

from .views import home_page, contact_page
from accounts.views import RegisterView, login_page
from django.contrib.auth import views as auth_views
from products.views import ProductListView
from products.views import ProductDetailView

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home_page, name='home'),
    path('contact/', contact_page),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', auth_views.LogoutView.as_view(template_name="auth/logout.html"), name='logout'),
    path('login', login_page, name='login'),
    path('admin/', admin.site.urls),
    path('products/', ProductListView.as_view()),
    path('products/<int:pk>', ProductDetailView.as_view(), name='detailed'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
