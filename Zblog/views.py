from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, CommentForm


def register_user(request) -> RegisterForm:   
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {name}!')
            return redirect('/login/')
        error = form.errors
        return render(request, 'register.html', {"form": form})
    form = RegisterForm()
    return render(request, 'register.html', {"form": form})


@login_required
def index(request):
    if request.method == "POST":
        comment_form = CommentForm(request.POST, initial={"username": request.user})
        comment_form.fields['username'].disabled = True
        if comment_form.is_valid():
            comment_form.save()
            messages.success(request, "Yours comment has been sent. Check your email for replies.")
            return redirect('/comment_sent/')
        return render(request, "index.html", {"comment_form": comment_form})

    comment_form = CommentForm(initial={"username": request.user})
    comment_form.fields['username'].disabled = True
    return render(request, "index.html", {"comment_form": comment_form})


def comment_sent(request):
    return render(request, "comment_sent.html")