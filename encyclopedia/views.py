from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse, HttpResponseRedirect

from . import util

from random import randint


def index(request):

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def title(request, title):
    return render(request, "encyclopedia/title.html", {
        "page": util.get_entry(title)
    })


def search(request):
    if request.method == "POST":
        name = request.POST.get("q")
        if util.get_entry(name.upper()) is not None:
            return HttpResponseRedirect(reverse('title', args=[name]))
        else:
            result = []
            for res in util.list_entries():
                if name.upper() in res.upper():
                    result.append(res)
            if result is not None:
                return render(request, "encyclopedia/search.html", {
                    "pages": result
                })


def random(request):
    entries = util.list_entries()
    random_page = randint(0, len(entries)-1)
    return HttpResponseRedirect(reverse('title', args=[entries[random_page]]))


def create(request):
    pass
