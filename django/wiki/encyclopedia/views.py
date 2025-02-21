from django.shortcuts import render, redirect
from django import forms
from django.http import HttpResponseNotFound
import random
from . import util

class NewEntryForm(forms.Form):
    title = forms.CharField(label="Title", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label="Content", widget=forms.Textarea(attrs={'class': 'form-control'}))

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def search(request):
    query = request.GET.get("q", "").strip()  # 検索クエリを取得し、空白を削除

    if not query:
        return redirect("index")  # クエリが空ならホームにリダイレクト

    entry_content = util.get_entry(query)  # 完全一致するエントリーを取得

    if entry_content:
        return redirect("title:index", title=query)  # 完全一致すれば該当ページへ

    # 部分一致するエントリーをフィルタリング
    all_entries = util.list_entries()  # 全エントリーを取得
    matching_entries = [entry for entry in all_entries if query.lower() in entry.lower()]

    return render(request, "encyclopedia/search_results.html", {
        "query": query,
        "matching_entries": matching_entries,
    })

def create_entry(request):
    if request.method == "POST":
        form = NewEntryForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data["title"].strip()
            content = form.cleaned_data["content"]

            if util.get_entry(title):  # すでに同じタイトルのエントリが存在するかチェック
                return render(request, "encyclopedia/new_entry.html", {
                    "form": form,
                    "error": "An entry with this title already exists."
                })

            # エントリを保存
            util.save_entry(title, content)

            # 新しいページへリダイレクト
            return redirect("title:index", title=title)

    else:
        form = NewEntryForm()

    return render(request, "encyclopedia/new_entry.html", {"form": form})

def random_entry(request):
    entries = util.list_entries()  # すべてのエントリーを取得
    if not entries:
        return redirect("index")  # エントリーがない場合はホームに戻る

    random_title = random.choice(entries)  # ランダムに1つ選ぶ
    return redirect("title:index", title=random_title)  # 選ばれたエントリーページへリダイレクト
