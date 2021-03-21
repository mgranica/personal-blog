from django.shortcuts import render

from django.views.generic import(
    ListView, 
    DetailView,
)

from .models import Entry, Category

# Create your views here.

class EntryListView(ListView):

    template_name = "entry/list.html"
    context_object_name ='entries'
    paginate_by = 10

    
    def get_context_data(self, **kwargs):
        context = super(EntryListView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
    

    def get_queryset(self):
        kword = self.request.GET.get("kword", '')
        category = self.request.GET.get("category", "")
        # search query
        result = Entry.objects.search_entry(kword, category)
        return result


class EntryDetailView(DetailView):
    model = Entry
    template_name = "entry/detail.html"

