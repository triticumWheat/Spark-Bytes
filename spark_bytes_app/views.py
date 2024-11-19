from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView, CreateView

from .forms import CustomUserCreationForm, CustomAuthenticationForm, EventForm
from .models import Profile, Event

class EventListView(ListView):
    model = Event
    template_name = 'spark_bytes/all_events.html'
    context_object_name = 'events'


class ProfileListView(ListView):
    model = Profile
    template_name = 'spark_bytes/all_profiles.html'
    context_object_name = 'profiles'


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'spark_bytes/profile_detail.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = Event.objects.filter(created_by=self.object)
        return context

class EventDetailView(DetailView):
    model = Event
    template_name = 'spark_bytes/event_detail.html'
    context_object_name = 'event'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.object.created_by
        return context


class RegisterView(FormView):
    template_name = 'spark_bytes/register.html'
    form_class = CustomUserCreationForm

    def form_valid(self, form):
        user = form.save()
        Profile.objects.create(
            user=user,
            buid=form.cleaned_data['buid'],
            img=form.cleaned_data['img']
        )
        login(self.request, user)
        return redirect('all_events')


class CreateEventView(LoginRequiredMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = 'spark_bytes/create_event.html'
    success_url = '/events/'

    def form_valid(self, form):
        profile = Profile.objects.get(user=self.request.user)
        form.instance.created_by = profile
        return super().form_valid(form)


class CustomLoginView(LoginView):
    template_name = 'spark_bytes/login.html'
    authentication_form = CustomAuthenticationForm

    def get_success_url(self):
        return reverse_lazy('all_events')


class CustomLogoutView(LogoutView):
    next_page = 'login'