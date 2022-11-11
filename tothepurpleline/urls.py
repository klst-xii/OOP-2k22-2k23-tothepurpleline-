from django.contrib import admin
from django.urls import path, include
from django.urls import re_path


from .views import home_page, contact_page
from accounts.views import RegisterView, login_page, CustomUserDeleteView
from django.contrib.auth import views as auth_views
from products.views import ProductListView
from products.views import ProductDetailView
from products.views import ProductFeaturedListView
from products.views import ProductFeaturedDetailView
from products.views import ProductDetailSlugView
from socials.views import PostListView, PostDetailView, PostEditView, PostDeleteView, CommentDeleteView, ProfileView, ProfileEditView, AddFollower, RemoveFollower, AddLike, AddDislike, UserSearch, ListFollowers, AddCommentLike, AddCommentDislike

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home_page, name='home'),
    path('contact/', contact_page, name='contact'),
    path('register/', RegisterView.as_view(), name='register'),
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
    path('search/', UserSearch.as_view(), name='profile-search'),
    path('<int:pk>/delete/', CustomUserDeleteView.as_view(template_name='auth/delete.html'), name='delete'),


    path('', include(('products.urls', 'products'), namespace='products')),
    path('featured/', ProductFeaturedListView.as_view(), name='featured_list'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='detailed'),
    # path('featured/<int:pk>', ProductFeaturedDetailView.as_view(), name='featured_detailed'),
    re_path(r'^products/(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view()),
    # path('', include('django.contrib.auth.urls')),

    path('cart/', include(('shopping_cart.urls', 'shopping_cart'), namespace='shopping_cart')),
    # path('', include(('socials.urls', 'socials'), namespace='socials')),


    path("__reload__/", include('django_browser_reload.urls')),

]



if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)