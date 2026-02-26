from django.urls import path
from .import views

urlpatterns =[
    path('<int:category_id>/', views.post_by_category, name='post_by_category'),
    path('<slug:category_slug>/', views.post_by_category, name='post_by_category'),
]