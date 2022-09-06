
from django.urls import path, include
from . import views

urlpatterns = [
    path('create', views.create, name='create'),
    path('<int:product_id>', views.detail, name='details'),
    path('<int:product_id>/upvote', views.upvote, name='upvote'),

]
