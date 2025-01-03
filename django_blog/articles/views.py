from django.views.generic.base import View
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import redirect, render
from .forms import ArticleForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.shortcuts import get_object_or_404
from django.views.generic.edit import DeleteView

from .models import Articles


class ArticlesListView(ListView):
    # 表示するページのhtmlの指定
    template_name = 'articles/articles_list.html'
    # modelの指定
    model = Articles
    # オブジェクト名の指定
    context_object_name = 'articles_list'
    # リストの表示順序の指定
    ordering = ['-updated_at']

class ArticleCreateView(CreateView):
    # 表示するページのhtmlの指定
    template_name = 'articles/article_create.html'
    # modelの指定
    model = Articles
    # form_classの指定
    form_class = ArticleForm
    # 登録成功時のアクション
    success_url = reverse_lazy("articles:create_confirm")

class ArticleCreateConfirm(View):
    # HTTPの要求への応答を処理する。
    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST or None)
        # テンプレートに渡すのに必要
        context = {'form': form}
        if 'confirm' in request.POST:
            return render(request, 'articles/article_create_confirm.html', context)
        if 'back' in request.POST:
            return render(request, 'articles/article_create.html', context)
        if 'create' in request.POST:
            # フォームのバリデーションを実行
            if form.is_valid():
                form.save()
                return redirect('home')
            else:
                return render(request, 'articles/article_create.html', context)

class ArticleDetailView(DetailView):
    # 表示するページのhtmlの指定
    template_name = 'articles/article_detail.html'
    # modelの指定
    model = Articles
    # オブジェクト名の指定
    context_object_name = 'article'

class ArticleUpdateView(UpdateView):
    # 表示するページのhtmlの指定
    template_name = 'articles/article_edit.html'
    # modelの指定
    model = Articles
    # form_classの指定
    form_class = ArticleForm

    # 取得するデータに関する部分
    def get_context_data(self, **kwargs):
        kwargs['article_id'] = self.object.pk
        return super().get_context_data(**kwargs)

class ArticleUpdateConfirmView(View):
    # HTTPの要求への応答を処理する。
    def post(self, request, *args, **kwargs):
        article_instance = get_object_or_404(Articles, pk=kwargs['pk'])
        form = ArticleForm(request.POST or None, instance=article_instance)
        # テンプレートに渡すのに必要
        context = {'form': form, 'article': article_instance, 'article_id': kwargs['pk']}
        if 'confirm' in request.POST:
            return render(request, 'articles/article_edit_confirm.html', context)
        if 'back' in request.POST:
            return render(request, 'articles/article_cedit.html', context)
        if 'create' in request.POST:
            # フォームのバリデーションを実行
            if form.is_valid():
                form.save()
                return redirect('home')
            else:
                return render(request, 'articles/article_edit.html', context)

class ArticleDeleteView(DeleteView):
    # 表示するページのhtmlの指定
    template_name = 'articles/article_delete.html'
    # modelの指定
    model = Articles
    # 登録成功時のアクション
    success_url = reverse_lazy("articles:create_list")
    # オブジェクト名の指定
    context_object_name = 'article_delete'