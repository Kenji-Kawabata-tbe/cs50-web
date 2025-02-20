from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.core.files.storage import default_storage

# Create your views here.

from encyclopedia import util

#def index(request):
#    return HttpResponse("Hello, Brian!")

def index(request, title):
    content = util.get_entry(title)
    if content is None:
        return HttpResponseNotFound("Entry not found")
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

