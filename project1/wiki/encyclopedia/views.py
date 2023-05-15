from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def article_archive(request, title):
    entry = util.get_entry(title)
    if entry == None:
        title = "error"
        return render(request, "templates/error.html")
    else: 
        return render(request, entry, {})

