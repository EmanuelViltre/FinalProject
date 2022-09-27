from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserEditForm, AvatarForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from .models import Avatar
from .models import *
from .forms import *
from django.db.models import Q


# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Created User")
            return render(
                request,
                "blog/index.html",
            )
    else:
        form = UserRegisterForm()
    return render(request, "user/register.html", {"form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = request.POST["username"]
            password = request.POST["password"]

            usuario = authenticate(username=user, password=password)
            if usuario is not None:
                login(request, usuario)
                messages.info(request, "Welcome")
                return render(
                    request,
                    "blog/index.html",
                )
            else:
                messages.info(request, "Incorrect User or Password")
                return render(request, "user/login.html", {"form": form})
        else:
            messages.info(request, "Incorrect User or Password")
            return render(request, "user/login.html", {"form": form})
    else:
        form = AuthenticationForm()
        return render(request, "user/login.html", {"form": form})


@login_required
def editProfile(request):
    user = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            user.first_name = form.cleaned_data["first_name"]
            user.last_name = form.cleaned_data["last_name"]
            user.email = form.cleaned_data["email"]
            user.password1 = form.cleaned_data["password1"]
            user.password2 = form.cleaned_data["password2"]
            user.save()
            messages.info(request, "Edited Profile")
            return render(
                request,
                "blog/index.html",
            )
        else:
            form = UserEditForm(instance=user)
            return render(request, "user/editProfile.html", {"form": form})

    else:
        form = UserEditForm(instance=user)
        return render(request, "user/editProfile.html", {"form": form})


@login_required
def profile(request):
    return render(request, "user/profile.html", {"image": obteinAvatar(request)})


def uploadAvatar(request):
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            oldAvatar = Avatar.objects.filter(user=request.user)
            if len(oldAvatar) > 0:
                oldAvatar.delete()
            avatar = Avatar(user=request.user, image=form.cleaned_data["image"])
            avatar.save()
            return render(
                request,
                "blog/index.html",
                {
                    "user": request.user,
                    "menssage": "Avatar Changed",
                    "image": obteinAvatar(request),
                },
            )
    else:
        form = AvatarForm()
    return render(
        request,
        "user/uploadAvatar.html",
        {"form": form, "user": request.user, "image": obteinAvatar(request)},
    )


def obteinAvatar(request):
    list = Avatar.objects.filter(user=request.user)
    if len(list) != 0:
        image = list[0].image.url
    else:
        image = ""
    return image


@login_required
def messages_all(request):
    user = request.user
    messages = Messages.objects.filter(Q(receiver=user) | Q(sender=user)).order_by(
        "-sent_at"
    )
    received = messages.filter(receiver=user).order_by("-sent_at")
    sent = messages.filter(sender=user).order_by("-sent_at")

    context = {
        "title": "Inbox",
        "user": user,
        "messages": messages,
        "received": received,
        "sent": sent,
    }
    return render(request, "user/messages.html", context)


@login_required
def new_message(request):
    if request.method != "POST":
        form = MessageForm()
    else:
        form = MessageForm(data=request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.sender = request.user
            msg.save()
            return redirect("messages")

    context = {"form": form}
    return render(request, "user/new_msg.html", context)
