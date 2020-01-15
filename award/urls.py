from django.urls import path, re_path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('', views.signup, name='signup'),
    path('home/', views.index, name='home'),
    re_path(r'^login/', LoginView.as_view(), name='login'),
    re_path(r'^logout/', LogoutView.as_view(next_page='login'), name='logout'),
    re_path(r'^newproject/', views.new_project, name='new_project'),
    re_path(r'^profile/', views.profile, name='profile'),
    re_path(r'^updateprofile/', views.update_profile, name='update_profile'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)