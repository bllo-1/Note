from typing import List
# from django.db.models.query import QuerySet
# from django.forms.models import BaseModelForm
from django.shortcuts import render
# from django.typing import list
from django.http import Http404, HttpResponse
from django.views.generic import UpdateView, CreateView, ListView, DetailView
from .models import Notes
from .forms import NotesForm
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect
# Create your views here.

class NotesDeleteView(DeleteView):
    model=Notes
    success_url ='/note/notes'
    template_name = 'note/notes_delete.html'


class NotesUpdateView(UpdateView):
    model=Notes
    success_url= '/note/notes'
    form_class = NotesForm

class NotesCreateView(CreateView):
    model=Notes
    success_url= '/note/notes'
    form_class = NotesForm
    login_url = "/admin"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NotesListView(LoginRequiredMixin ,ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"
    login_url = "/admin"

    # def get_queryset(self):
    #     return self.request.user.all()

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"
