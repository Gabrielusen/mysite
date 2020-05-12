from django.urls import path
from .views import home, contact_view, success_view


urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact_view, name='contact'),
    path('success/', success_view, name='success'),
]
