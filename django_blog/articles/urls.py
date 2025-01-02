from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    # 記事の一覧画面 /articles
    path('', views.ArticlesListView.as_view(), name='articles_list'),
    # 記事の登録画面 /articles/create
    path('create/', views.ArticleCreateView.as_view(), name='article_create'),
    # 記事の登録内容確認画面 /articles/create_confirm
    path('create_confirm', views.ArticleCreateConfirm.as_view(), name='article_create_confirm'),
    # 記事の詳細画面 /articles/{id}
    path('<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'),
    # 記事の編集画面 /articles/{id}/edit
    path('<int:pk>/edit/', views.ArticleUpdateView.as_view(), name='article_edit'),
    # 記事の編集内容確認画面 /articles/{id}/edit_confirm
    path('<int:pk>/edit_confirm', views.ArticleUpdateConfirmView.as_view(), name='article_edit_confirm'),
    # 記事の削除確認画面 /articles/{id}/delete_confirm
    path('<int:pk>/delete_confirm', views.ArticleDeleteView.as_view(), name='article_delete'),
]