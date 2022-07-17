

from django.urls import path
from . import views

#   from .views import PostCreateView, AuthorDeleteView, AuthorUpdateView
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.index, name='index'),
    #   path('posts/', views.PostListView.as_view(), name='posts'),
    path('blogs/', views.PostListView.as_view(), name='blogs'),
    path('blog/<int:pk>', views.PostDetailView.as_view(), name='blog-detail'),
    path('bloggers/', views.AuthorListView.as_view(), name='bloggers'),
    path('blogger/<int:pk>', views.AuthorDetailView.as_view(), name='blogger-detail'),
]


urlpatterns += [
    path('mytrollings/', views.CommentedPostsByUserListView.as_view(), name='my-trollings'),
]

urlpatterns += [
    #   path('create/<slug:slug>', views.create_post_author, name='create-post-author'),
    #   path('blog/add/', PostCreateView.as_view(), name='blog-add'),
    path('create/', views.PostCreate.as_view(), name='blog_create'),
    path('blog/create/', views.CommentCreate.as_view(), name='comment_create'),
]





