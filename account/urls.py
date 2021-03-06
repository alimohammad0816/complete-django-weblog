from django.contrib.auth import views
from django.urls import path
from .views import ArticleList,ArticleCreate,ArticleUpdate,ArticleDelete,Profile,Login

app_name = 'account'
urlpatterns = [
    path('',ArticleList.as_view(),name='home'),
    path('article/create/',ArticleCreate.as_view(),name='create'),
    path('article/update/<int:pk>',ArticleUpdate.as_view(),name='update'),
    path('article/delete/<int:pk>',ArticleDelete.as_view(),name='delete'),
    path('profile/',Profile.as_view(),name='profile'),
]