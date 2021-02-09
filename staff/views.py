from django.shortcuts import render
from .models import  Staff
from .filters import CategoryFilter


def staff_list(request):
    staffs = Staff.objects.all()
    myFilter = CategoryFilter(request.GET, queryset=staffs)
    staffs = myFilter.qs


    context = {
        'staffs': staffs,
        'myfilter': myFilter
    }

    return render(request, 'staff/staff_list.html', context)


def staff_detail(request, slug):
    query = Staff.objects.filter(slug__iexact=slug)
    if query.exists():
        query = query.first()
    context = {
        'staff': query
    }
    return render(request, 'staff/staff_detail.html', context)