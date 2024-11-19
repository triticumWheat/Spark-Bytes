"""spark_bytes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from spark_bytes import settings
from spark_bytes_app.views import EventDetailView, ProfileDetailView, EventListView, ProfileListView, CustomLoginView, \
    CustomLogoutView, RegisterView, CreateEventView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', EventListView.as_view(), name='all_events'),
    path('events/', EventListView.as_view(), name='all_events'),
    path('profiles/', ProfileListView.as_view(), name='all_profiles'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile_detail'),
    path('event/<int:pk>/', EventDetailView.as_view(), name='event_detail'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('create_event/', CreateEventView.as_view(), name='create_event'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)