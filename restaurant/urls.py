from django.urls import path
from .views import sign_in, log_in

urlpatterns = [
    path('sign-in/', sign_in, name='sign-in'),
    path('log-in/', log_in, name='log-in'),
]
