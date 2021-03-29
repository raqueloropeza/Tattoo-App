from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.main),
    path('register',views.register),
    path('register/create', views.createUser),
    path('register/profile', views.newProfile),
    path('new/profile/create', views.createProfile),
    path('profile', views.ProfilePage)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)