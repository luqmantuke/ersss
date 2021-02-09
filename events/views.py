from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Events
from blog.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def events_list(request):
    events = Events.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(events, 15)

    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        events = paginator.page(1)
    except EmptyPage:
        events = paginator.page(paginator.num_pages)

    context = {
        'events': events
    }

    return render(request, 'events/events.html', context)


def event_detail(request, slug):
    query = Events.objects.filter(slug__iexact=slug)
    if query.exists():
        query = query.first()
    else:
        return render(request, '404.html', status=404)

    context = {
        'event': query
    }
    return render(request, 'events/event_detail.html', context)
