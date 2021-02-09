from django.shortcuts import render, redirect
from .forms import OlevelForm, AlevelForm
from django.contrib import messages
from django.urls import reverse
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from TukeSchool import settings


def applications(request):
    return render(request, 'application/application.html')


def olevel(request):
    form = OlevelForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            Full_Name = form.cleaned_data['Full_name']
            contact_message = f'Student  "{Full_Name}" just applied for Ordinary Level. Please review his or her application and contact him as soon as possible.'

            try:
                send_mail("O-level application", contact_message, settings.EMAIL_HOST_USER, ['tuke.luqman@gmail.com'],
                          settings.FAIL_SILENTLY)
            except BadHeaderError:
                return HttpResponse('Invalid Header.')
            form.save()
            messages.success(request, f'Congratulations {Full_Name}. You Successfully applied for Ordinary Level. We will contact you as soon as possible for the interview.')

            return redirect('home')

    context = {
        'form': form
    }
    return render(request, 'application/olevel.html', context)


def alevel(request):
    form = AlevelForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            Full_Name = form.cleaned_data['Full_name']
            contact_message = f'Student  "{Full_Name}" just applied for Advanced Level. Please review his application and contact him as soon as possible.'

            try:
                send_mail("A-level application", contact_message, settings.EMAIL_HOST_USER, ['tuke.luqman@gmail.com'],
                          settings.FAIL_SILENTLY)
            except BadHeaderError:
                return HttpResponse('Invalid Header.')
            form.save()
            messages.success(request,
                             f'Congratulations {Full_Name}. You Successfully applied for Advanced Level. We will contact you as soon as possible for the interview.')

            return redirect('home')

    context = {
        'form': form
    }
    return render(request, 'application/alevel.html', context)