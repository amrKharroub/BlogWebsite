from django.urls import path
from .views import HomeView, PostDetails

urlpatterns = [
    path("", HomeView.as_view(), name="homepage"),
    path("article/<str:slug>/", PostDetails.as_view(), name="post-detail"),
]
