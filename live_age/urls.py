from django.urls import path
from .views import live_age_view, get_live_age

urlpatterns = [
    path('', live_age_view),
    path('api/', get_live_age),
]
