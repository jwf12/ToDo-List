from django.shortcuts import render
from django.views import generic
from .models import Tareas
from .forms import TareasForm

class Home(generic.TemplateView):
    template_name = 'home.html'
    context_object_name = 'tareas'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tareas'] = Tareas.objects.filter(usuario = self.request.user)
        return context

    
class TareasView(generic.CreateView):
    template_name = 'todo.html'
    form_class = TareasForm
    success_url = 'home.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
