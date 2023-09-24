from django.shortcuts import render
from django.views.generic import ListView
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
