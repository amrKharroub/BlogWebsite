from typing import Any
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


# Create your views here.
class HomeView(ListView):
    model = Post
    context_object_name = "posts"
    paginate_by = 10

    def get_template_names(self) -> list[str]:
        if self.request.htmx:
            return [
                "blog/components/list_elements.html",
            ]
        return [
            "blog/index.html",
        ]


class PostDetails(DetailView):
    model = Post
    context_object_name = "post"
    template_name = "post.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["related"] = Post.objects.filter(author=self.get_object().author)[:5]
        return context

    pass
