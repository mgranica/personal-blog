import datetime
#
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from django.views.generic import (
    TemplateView,
    CreateView
)

from applications.entry.models import Entry

from .models import Home

from .forms import SubcriberForm, ContactForm


class HomePageView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)

        context['home'] = Home.objects.latest('created')
        context['cover'] = Entry.objects.entry_cover()
        context['home_entries'] = Entry.objects.home_entries()
        context['recent_entries'] = Entry.objects.recent_entries()
        context['form'] = SubcriberForm
        return context



class SubcriberCreateView(CreateView):
    form_class = SubcriberForm
    success_url = '.'

class ContactCreateView(CreateView):
    form_class = ContactForm
    success_url = '.'