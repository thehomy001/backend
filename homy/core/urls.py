from django.urls import path
from core import views

urlpatterns = [
  path('contact/', views.ContactView.as_view(), name='contact'),
  path('contact/list', views.ContactView.as_view(), name='list'),

]