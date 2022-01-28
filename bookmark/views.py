from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .models import Bookmark

# Create your views here.
class BookmarkListView(ListView):
    model = Bookmark
    paginate_by = 5 #5개씩 보여줌

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list') #list = BookmarkListView.as_view()
    template_name_suffix = '_create' #생성한 순서대로 정렬

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'  # 업데이트한 순서대로 정렬

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')  # list = BookmarkListView.as_view() 삭제 후 이 페이지로 이동