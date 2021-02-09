from django.shortcuts import render
from staff.models import Staff
from events.models import Events
from blog.models import Post


def home(request):
    events = Events.objects.all()[0:3]
    staffs = Staff.objects.filter(category="Teaching Staff")[0:4]
    posts = Post.objects.filter(status="Published")[0:3]
    context = {
        'events': events,
        'staffs': staffs,
        'posts': posts,
    }
    return render(request, 'index.html', context)


def aboutus(request):
    staffs = Staff.objects.all()[0:8]
    context = {
        'staffs': staffs
    }
    return render(request, 'about.html', context)

def handler404(request, exception):
    return render(request, '404.html', status=404)
#
#
# def handler403(request, exception):
#     return render(request, '403.html', status=403)
#
#
# def handler400(request, exception):
#     return render(request, '400.html', status=400)
#
#


def handler500(request):
    return render(request, '500.html', status=500)
