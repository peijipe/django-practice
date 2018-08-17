from django.urls import include, path

from . import views

app_name = 'news'

urlpatterns = [
    path('', views.title_get, name='post_list'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('json/', views.json_page, name='json_page')
]
