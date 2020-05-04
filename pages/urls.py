from django.urls import path
from .views import HomePageView, contact_view, success_view


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('contact/', contact_view, name='contact'),
    path('success', success_view, name='success'),
]
