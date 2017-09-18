from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    all_posts=Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts':posts, "all_posts":all_posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    all_posts=Post.objects.all()
    return render(request, 'blog/post_detail.html', {'post': post, "all_posts":all_posts})


def post_from(request, year, month, day):
    posts = Post.objects.filter(created_date__day=day).filter(created_date__month=month).filter(created_date__year=year)
    all_posts=Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts, "all_posts":all_posts})

def post_new(request):
    all_posts=Post.objects.all()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form, "all_posts":all_posts})

def search(request):
    title=request.GET["search"]
    posts = Post.objects.filter(title__icontains=title)
    all_posts=Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts, "all_posts":all_posts})


