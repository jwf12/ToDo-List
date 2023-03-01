from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tareas
from .forms import TareasForm
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse, reverse_lazy

class Home(LoginRequiredMixin ,generic.TemplateView):
    template_name = 'home.html'
    context_object_name = 'tareas'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tareas'] = Tareas.objects.filter(usuario = self.request.user)
        return context

    
class TareasView(generic.CreateView):
    model = Tareas
    form_class = TareasForm
    success_url = reverse_lazy('home.html')
    template_name = 'home.html'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('todo:home')

    
class TareaDeleteView(generic.DeleteView):
    model = Tareas
    success_url = reverse_lazy('todo:home')


class TareaEditarView(generic.UpdateView):
    model = Tareas
    success_url = reverse_lazy('todo:home')
    fields = [
        'titulo',
        'descripcion',
        'fecha_limite',
    ]

    def form_valid(self, form):
        return super().form_valid(form)
    
    def form_invalid(self,form):
        return super().form_invalid(form)
    

class CustomLoginView(LoginView):
    def form_invalid(self, form):
        messages.error(self.request, 'Credenciales no validas.')        
        return super().form_invalid(form)
    

class SingUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('todo:login')
    template_name = 'register.html'

    def form_valid(self, form):        
        response = super().form_valid(form)
        messages.success(self.request, '¡Tu cuenta ha sido creada! Por favor inicia sesión.')
        return response
            
    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request, 'Las contraseñas no coinciden.')        
        return response