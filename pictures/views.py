from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Page

class PageList(ListView):
    model = Page
    template_name = "page_list.html"

    # def get_context_data(self, **kwargs):
    #     context = Page.objects.all()
    #     return context