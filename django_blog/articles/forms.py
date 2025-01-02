from django import forms

from .models import Articles


class ArticleForm(forms.ModelForm):
    class Meta:
        # 対象のモデルを指定
        model = Articles
        # 登録するカラムの指定
        fields = ['title', 'article_body']
        # ラベルを設定
        labels = {
            'title': 'タイトル',
            'article_body': '記事本文',
        }
        # プレースホルダーを設定
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': '50字以内で入力してください'
            }),
            'article_body': forms.Textarea(attrs={
                'placeholder': '1万字以内で入力してください',
                'cols': '30',
                'rows': '10',
            }),
        }