from django.urls import path
from . import views

urlpatterns = [
    path('blog_posts', views.index, name='index'),
    path('post_details/<int:post_id>/', views.post_details, name='post_details'),
    path('create/', views.post_create, name='post_create'),
    path('edit/<int:pk>/', views.post_edit, name='post_edit'),
    path('delete/<int:pk>/', views.post_delete, name='post_delete'),
    path('signup/', views.signup, name='signup'),
    path('', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
]
