import markdown2
from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from django.core.files.storage import default_storage
from django import forms

# Create your views here.

from encyclopedia import util

#def index(request):
#    return HttpResponse("Hello, Brian!")

def index(request, title):
    content = util.get_entry(title)
    if content is None:
        return HttpResponseNotFound("Entry not found")
    # Markdown を HTML に変換
    content = markdown2.markdown(content)
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": content
    })


#def entry(request, title):
#    try:
#        f = default_storage.open(f"entries/{title}.md")
#        content = f.read().decode("utf-8")
#        return render(request, "title/entry.html", {
#            "title": title,
#            "content": content
#        })
#    except FileNotFoundError:
#        return HttpResponseNotFound("Entry not found")

#def index(request):
#    return render(request, "encyclopedia/index.html", {
#        "entries": util.get_entry(css)
#    })

# フォームの定義
class EditEntryForm(forms.Form):
    content = forms.CharField(label="Content", widget=forms.Textarea(attrs={'class': 'form-control'}))

# エントリー編集ビュー
def edit_entry(request, title):
    entry_content = util.get_entry(title)  # 既存のエントリを取得

    if entry_content is None:
        return render(request, "encyclopedia/error.html", {
            "message": f"The page '{title}' does not exist."
        })

    if request.method == "POST":
        form = EditEntryForm(request.POST)

        if form.is_valid():
            new_content = form.cleaned_data["content"]
            util.save_entry(title, new_content)  # 編集内容を保存

            return redirect("title:index", title=title)  # 保存後にエントリページへリダイレクト

    else:
        form = EditEntryForm(initial={"content": entry_content})  # 既存の内容を初期値として設定

    return render(request, "encyclopedia/edit_entry.html", {
        "form": form,
        "title": title
    })
