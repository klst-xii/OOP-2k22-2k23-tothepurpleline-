from django.contrib import admin
from django.urls import path, include
from django.urls import re_path

from accounts import views
from .views import home_page, contact_page
from accounts.views import *
from django.contrib.auth import views as auth_views
from products.views import ProductListView
from products.views import ProductDetailView
from products.views import ProductFeaturedListView
# from products.views import ProductFeaturedDetailView
from products.views import ProductDetailSlugView
from socials.views import *

from django.conf import settings
from django.conf.urls.static import static

from cart.views import add_to_cart
from cart.views import cart_home, decrease_cart, increase_cart, remove_from_cart

# app_name = 'cart'

urlpatterns = [
    path('', home_page, name='home'),
    path('contact/', contact_page, name='contact'),
    path('register/', RegisterView.as_view(), name='register'),
    path('featured/', ProductFeaturedListView.as_view(), name='featured_list' ),
    # path('featured/<int:pk>', ProductFeaturedDetailView.as_view(), name='featured_detailed'),

    path('logout/', auth_views.LogoutView.as_view(template_name="auth/logout.html"), name='logout'),
    path('login', login_page, name='login'),
    path('admin/', admin.site.urls),
    path('socials/', PostListView.as_view(), name='post-list'),
    path('socials/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('socials/edit/<int:pk>/', PostEditView.as_view(), name='post-edit'),
    path('socials/<int:pk>/followers/', ListFollowers.as_view(), name='list-followers'),
    path('socials/delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
    path('socials/<int:post_pk>/comment/delete/<int:pk>/', CommentDeleteView.as_view(), name='comment-delete'),
    path('socials/<int:post_pk>/comment/<int:pk>/like', AddCommentLike.as_view(), name='comment-like'),
    path('socials/<int:post_pk>/comment/<int:pk>/dislike', AddCommentDislike.as_view(), name='comment-dislike'),
    path('socials/<int:pk>/like', AddLike.as_view(), name='like'),
    path('socials/<int:pk>/dislike', AddDislike.as_view(), name='dislike'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/edit/<int:pk>/', ProfileEditView.as_view(), name='profile-edit'),
    path('profile/<int:pk>/followers/add', AddFollower.as_view(), name='add-follower'),
    path('profile/<int:pk>/followers/remove', RemoveFollower.as_view(), name='remove-follower'),
    # path('profile/edit/<int:pk>/', views.user_delete, name='delete'),
    path('search/', UserSearch.as_view(), name='profile-search'),

    path('cart/', include(('cart.urls', 'cart'), namespace='cart')),
    path('payment/', include(('payment.urls', 'payment'), namespace='payment')),
    path('products/', include(('products.urls', 'products'), namespace='products')),

    path("__reload__/", include('django_browser_reload.urls')),

    # path('products/', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='detailed'),
    re_path(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view()),

    # path('cart/', cart_home, name='cart-home'),
    path('cart/decrease-item/<int:pk>/', decrease_cart, name='decrease-item'),
    path('cart/increase-item/<int:pk>/', increase_cart, name='increase-item'),
    path('cart/remove-item/int<int:pk>/', remove_from_cart, name='remove-item'),
    path('cart/<int:pk>/add', add_to_cart, name='add'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)