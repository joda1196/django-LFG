from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *

from django.contrib.auth.decorators import login_required
from .decorators import unauthorized_user

# Create your views here.


@unauthorized_user
def registerPage(request):
    userform = CreateUserForm()
    if request.method == "POST":
        userform = CreateUserForm(request.POST)
        if userform.is_valid():
            user = userform.save()
            username = userform.cleaned_data.get("username")
            messages.success(
                request, "Account was successfully created for " + username
            )
            return redirect("login")

    context = {"userform": userform}
    return render(request, "accounts/register.html", context)


@unauthorized_user
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("homepage", "all-posts")
        else:
            messages.info(request, "Username or Password is invalid")
    return render(request, "accounts/login.html")


def logoutUser(request):
    logout(request)
    return redirect("homepage", "all-posts")


def redirect_home(request):
    return redirect("homepage", "all-posts")


def home(request, platform):
    if platform == "all-posts":
        posts = Post.objects.all()
    else:
        posts = Post.objects.filter(platform=platform)

    is_mod = request.user.groups.filter(name="Moderator").exists()
    context = {"posts": posts, "is_mod": is_mod}
    return render(request, "base.html", context)


@login_required
def user_posts(request):
    user_posts = Post.objects.filter(author=request.user)
    context = {"user_posts": user_posts}
    return render(request, "my-posts.html", context)


@login_required
def create_post(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():

            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("homepage", "all-posts")

    context = {"form": form}
    return render(request, "createpost.html", context)


@login_required
def update_post(request, pk):
    form = PostForm()
    current_post = Post.objects.get(id=pk)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            current_post.header = form.cleaned_data["header"]
            current_post.platform = form.cleaned_data["platform"]
            current_post.save()
            return redirect("homepage", "all-posts")

    context = {"form": form, "current_post": current_post}
    return render(request, "updatepost.html", context)


def delete_post(request, pk):
    current_post = Post.objects.get(id=pk)
    current_post.delete()
    messages.success(request, "Post Successfully Deleted")
    return redirect("homepage", "all-posts")
