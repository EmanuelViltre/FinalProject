from django.urls import path
from .views import *
from user.views import messages_all, new_message


urlpatterns = [
    path("article/<str:slug>", detail, name="detail"),
    path("create", createPost, name="create"),
    path("update-post/<str:slug>", updatePost, name="updatepost"),
    path("delete-post/<str:slug>", deletePost, name="deletepost"),
    path("about", about, name="about"),
    path("inbox/", messages_all, name="messages"),
    path("inbox/new_msg/", new_message, name="newmessage"),
]
