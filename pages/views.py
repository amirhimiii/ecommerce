from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from .forms import ContactForm
from django.views import generic


class AboutUsView(TemplateView):
    template_name = "pages/about_us.html"



class ContactView(generic.CreateView):
    form_class = ContactForm
    template_name = "pages/contact_us.html"
    success_url = reverse_lazy('feedback')



def feedback(request):
    return render(request,'pages/feedback.html')





