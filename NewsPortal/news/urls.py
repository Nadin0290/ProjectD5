from django.urls import path
from .views import PostList, PostDetailView, PostSearch, PostUpdateView, PostDeleteView, PostCreateView


urlpatterns = [
    path('', PostList.as_view()), # Ссылка на вкладку всех новостей "News"
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'), # Ссылка на детали новости
    path('search/', PostSearch.as_view(), name='search'), # Ссылка на вкладку "Поиск"
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('update/<int:pk>', PostUpdateView.as_view(), name='post_update'),  # Ссылка на создание новости
    path('delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
]
