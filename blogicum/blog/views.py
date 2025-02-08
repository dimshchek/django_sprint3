from django.shortcuts import render, get_object_or_404
from django.utils.timezone import now

from .constants import INDEX_NUMBER_OF_POSTS
from .models import Post, Category


def get_published_posts():
    return Post.objects.filter(
        is_published=True,
        pub_date__lte=now(),
        category__is_published=True
    )


def index(request):
    """Главная."""
    context = {'post_list': get_published_posts()[:INDEX_NUMBER_OF_POSTS]}
    return render(request, 'blog/index.html', context)


def post_detail(request, post_id):
    """Детали поста."""
    post = get_object_or_404(
        get_published_posts(),
        id=post_id
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
    posts = get_published_posts().filter(
        category=category,
    )
    context = {
        'post_list': posts,
        'category': category
    }
    return render(request, 'blog/category.html', context)
