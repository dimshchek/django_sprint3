from .models import Post

from django.utils.timezone import now
from django.shortcuts import render, get_object_or_404
from .models import Post, Category


def index(request):
    """Главная."""
    post_list = Post.objects.filter(
        is_published=True,
        pub_date__lte=now(),
        category__is_published=True
    ).order_by('-created_at')[:5]
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)


def post_detail(request, post_id):
    """Детали поста."""
    post = get_object_or_404(
        Post,
        id=post_id,
        is_published=True,
        pub_date__lte=now(),
        category__is_published=True
    )
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    """Поиск по категориям."""
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    posts = Post.objects.filter(
        category=category,
        is_published=True,
        pub_date__lte=now()
    ).order_by('-created_at')
    context = {
        'post_list': posts,
        'category': category
    }
    return render(request, 'blog/category.html', context)
