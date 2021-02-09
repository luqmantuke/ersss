from .models import Post
from django.shortcuts import render
from events.models import Events
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def post_list(request):
    posts = Post.objects.filter(status="Published")
    events = Events.objects.all()[0:3]
    popular_posts = Post.objects.filter(popular="Popular")[0:3]
    recent_post = Post.objects.filter(status="Published")[0:3]
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 15)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts,
        'events': events,
        'popular_posts': popular_posts,
        'recent_posts': recent_post
    }

    return render(request, 'blog/post_list.html', context)


def post_detail(request, slug):
    query = Post.objects.filter(slug__iexact=slug)
    events = Events.objects.all()[0:3]
    popular_posts = Post.objects.filter(popular="Popular")[0:3]
    recent_post = Post.objects.filter(status="Published")[0:3]

    if query.exists():
        query = query.first()

    context = {
        'post': query,
        'events': events,
        'popular_posts': popular_posts,
        'recent_posts': recent_post
    }

    return render(request, 'blog/post_detail.html', context)
