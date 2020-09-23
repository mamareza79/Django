from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse, HttpResponseRedirect

from . import util


def index(request):
    if request.method == "POST":
        name = request.POST.get("q")
        if util.get_entry(name) is not None:
            return HttpResponseRedirect(reverse('title', args=[name]))
        else:
            result = []
            for res in util.list_entries():
                if name in res:
                    result.append(res)
            if result is not None:
                # return render(request, "encyclopedia/search.html", {
                # "pages": result
                # })
                return HttpResponseRedirect(reverse('search', args=result))
                # pass
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def title(request, title):
    return render(request, "encyclopedia/title.html", {
        "page": util.get_entry(title)
    })


def search(request, pages):
    # list_entries = util.list_entries()
    print(pages)
    return render(request, "encyclopedia/search.html", {
        "pages": pages
    })


def create(request):
    pass
