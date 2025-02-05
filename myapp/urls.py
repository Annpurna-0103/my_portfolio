from django.urls import path
from . import views  # Your views import

urlpatterns = [
    # Add your views here
    path('', views.index, name='index'),  # example home page URL pattern
]
