from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('setting', views.setting, name='setting'),
    path('delete/<int:id>', views.delete, name='delete'),
]