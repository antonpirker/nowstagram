from django.urls import include, path

from views import about, index

urlpatterns = [
    path('', index),
    path('about', about),
    path('api/', include('api.urls')),
]
