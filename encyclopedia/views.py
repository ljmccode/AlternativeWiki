from django.shortcuts import render
from markdown2 import Markdown

from . import util

markdowner = Markdown()


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, title):

    htmlTitle = markdowner.convert(util.get_entry(title))
    return render(request, "encyclopedia/title.html", {
        "title": htmlTitle
    })