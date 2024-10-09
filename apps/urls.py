from django.urls import path, include

urlpatterns = [
    path('users', include('users.urls')),
    path('shops', include('shops.urls'))
]
