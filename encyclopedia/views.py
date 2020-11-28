from django.shortcuts import render
from markdown2 import Markdown
from django.http import HttpResponse

from . import util

markdowner = Markdown()


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, title):
    try:
        htmlTitle = markdowner.convert(util.get_entry(title))
    except: 
        return render(request, "encyclopedia/404.html", {
            "title": title
        })
    return render(request, "encyclopedia/title.html", {
        "title": htmlTitle,
        "entry_name": title
        })