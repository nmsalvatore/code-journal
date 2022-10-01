from django.urls import path
from .views import home, new_post, edit_post, delete_post, filter_by_tag, PostDetailView

urlpatterns = [
    path('', home, name='home'),
    path('post/new/', new_post, name='new-post'),
    path('post/edit/<int:pk>/', edit_post, name='edit-post'),
    path('post/delete/<int:pk>/', delete_post, name='delete-post'),
    path('tags/<str:tag>/', filter_by_tag, name='filter-by-tag'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='view-post'),
]