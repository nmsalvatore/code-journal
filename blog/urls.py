from django.urls import path
from . import views

urlpatterns = [
    path('', views.auth_redirect),
    path('posts/all/', views.home, name='home'),
    path('post/new/', views.new_post, name='new-post'),
    path('post/edit/<int:pk>/', views.edit_post, name='edit-post'),
    path('post/delete/<int:pk>/', views.delete_post, name='delete-post'),
    path('posts/filter-by-tag/<str:tag>/', views.filter_by_tag, name='filter-by-tag'),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='view-post'),
]
