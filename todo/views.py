from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic

from todo.models import Tag


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "todo/index.html")


class TagListView(generic.ListView):
    model = Tag
