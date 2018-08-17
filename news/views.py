from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .form import PostForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def json_page(request):
    username = request.body
    data = json.loads(username.decode('utf-8'))
    dic = {"uname": data}
    return render(request, 'news/json_page.html', dic)


@login_required
def title_get(request):
    post_dic = {"results": []}
    input_value = request.GET.get("title")

    if input_value is None:
        posts = Post.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')
        return render(request, 'news/post_list.html', {'posts': posts})

    news = Post.objects.filter(title__contains=input_value)
    for topic in news:
        if input_value in topic.title:
            result = {
                "title": topic.title,
                "text": topic.body,
                "date": topic.pub_date,
                "image": topic.image
            }
            post_dic["results"].append(result)

    return render(request, 'news/post_list.html', post_dic)


@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'news/post_detail.html', {'post': post})


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('news:post_detail', pk=post.pk)

    else:
        form = PostForm()

    return render(request, 'news/post_edit.html', {'form': form})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('news:post_detail', pk=post.pk)

    else:
        form = PostForm(instance=post)

    return render(request, 'news/post_edit.html', {'form': form})