from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
from django.contrib import messages
from django.shortcuts import render, redirect

from django.http import HttpResponse

def empty_favicon(request):
    return HttpResponse('', content_type='image/x-icon')


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = ContactForm()
#     return render(request, 'contact.html', {'form': form})





def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            form.save()
            messages.success(request, 'Your message was sent successfully!')
            return redirect('contact')  # Redirect to the same page to avoid form resubmission
        else:
            messages.error(request, 'There was a problem with your submission. Please correct the errors below.')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})