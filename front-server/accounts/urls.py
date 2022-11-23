from django.urls import path
from . import views

urlpatterns = [
    path('<int:user_pk>/', views.userdetail),
    path('<int:user_pk>/mvti/<int:mvti_pk>/', views.usermvti),
]