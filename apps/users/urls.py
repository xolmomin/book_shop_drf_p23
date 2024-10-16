from django.urls import path

from users.views import AddressListCreateAPIView, RegisterCreateAPIView, LoginAPIView, UserActivateAPIView, \
    AddressDestroyUpdateAPIView

urlpatterns = [
    path('address', AddressListCreateAPIView.as_view(), name='address_list'),
    path('address/<int:pk>', AddressDestroyUpdateAPIView.as_view(), name='address_detail'),

    path('register', RegisterCreateAPIView.as_view(), name='register'),
    path('login', LoginAPIView.as_view(), name='login'),
    path('activate/<uidb64>/<token>', UserActivateAPIView.as_view(), name='activate_user'),

]
