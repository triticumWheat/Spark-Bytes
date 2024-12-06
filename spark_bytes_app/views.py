from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView, CreateView
from django.http import JsonResponse
from django.contrib.auth.mixins import UserPassesTestMixin

from .forms import CustomUserCreationForm, CustomAuthenticationForm, EventForm
from .models import Profile, Event

class EventListView(ListView):
    model = Event
    template_name = 'spark_bytes/all_events.html'
    context_object_name = 'events'

    def get_queryset(self):
        queryset = super().get_queryset()

        # Get search parameters
        name = self.request.GET.get('name', '')
        location = self.request.GET.get('location', '')
        date = self.request.GET.get('date', '')
        food_types = self.request.GET.getlist('food_types')  # Get list of selected food types
        allergies = self.request.GET.getlist('allergies')  # Get list of selected allergies

        # Filter based on search parameters
        if name:
            queryset = queryset.filter(name__icontains=name)
        if location:
            queryset = queryset.filter(location__icontains=location)
        if date:
            queryset = queryset.filter(date__date=date)
        if food_types:
            # Filter events that match ANY of the selected food types
            queryset = queryset.filter(food_types__in=food_types)
        if allergies:
            for allergy in allergies:
                queryset = queryset.filter(allergies__icontains=allergy)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Provide food types and allergies lists to the template
        context['food_types'] = [
            "Italian", "Mediterranean", "Salad", "American", "BBQ", 
            "Chinese", "Korean", "Japanese", "Mexican", "Spanish", 
            "Indian", "Thai", "Vietnamese", "Sushi", "Breakfast", 
            "Lunch", "Vegan", "Vegetarian"
        ]
        context['allergies'] = [
            "Dairy", "Soy", "Nuts", "Fish", "Shellfish", "Eggs", 
            "Wheat", "Sesame"
        ]
        # Pass the selected values back to the template
        context['selected_food_types'] = self.request.GET.getlist('food_types')
        context['selected_allergies'] = self.request.GET.getlist('allergies')
        return context



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
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic import FormView
from .forms import CustomUserCreationForm
from .models import Profile


class RegisterView(FormView):
    template_name = 'spark_bytes/register.html'
    form_class = CustomUserCreationForm

    def form_valid(self, form):
        # Save the new user
        user = form.save()

        # Create a new Profile for the user
        Profile.objects.create(
            user=user,
            buid=form.cleaned_data['buid'],
            img=form.cleaned_data['img']
        )

        # Log the user in immediately after registration
        login(self.request, user)

        # Redirect to the 'all_events' page after successful registration
        return redirect('all_events')

    def form_invalid(self, form):
        # This method will be triggered if the form is invalid
        print(form.errors)  # Log the errors if needed for debugging
        return super().form_invalid(form)


class CreateEventView(LoginRequiredMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = 'spark_bytes/create_event.html'
    success_url = '/events/'

    def form_valid(self, form):
        profile = Profile.objects.get(user=self.request.user)
        form.instance.created_by = profile
        return super().form_valid(form)




from django.shortcuts import render
from .utils import generate_qr_code  # Import the QR code generation function

from django.shortcuts import render
from django.http import JsonResponse
from .utils import generate_qr_code

from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags

class ReserveSpotView(LoginRequiredMixin, DetailView):
    model = Event
    template_name = 'spark_bytes/event_detail.html'
    context_object_name = 'event'

    def post(self, request, *args, **kwargs):
        event = self.get_object()
        profile = Profile.objects.get(user=request.user)

        # Check if the event is full
        if event.is_full():
            return JsonResponse({'message': 'This event is full. No more spots are available.'}, status=400)

        # Check if the user has already reserved a spot
        if profile in event.reserved_by.all():
            return JsonResponse({'message': 'You have already reserved a spot for this event.'}, status=400)

        # Add the profile to the reservation list
        event.reserved_by.add(profile)

        # Generate QR code
        unique_data = f"{profile.user.email}_{event.id}"
        qr_code_data = generate_qr_code(unique_data)

        # Send email with QR code
        self.send_qr_code_email(profile.user.email, event, qr_code_data)

        # Save and reload event to ensure consistency
        event.save()
        return JsonResponse({
            'message': 'Reservation successful!',
            'qr_code': qr_code_data
        }, status=200)

    def send_qr_code_email(self, user_email, event, qr_code_data):
        """Send an email with the QR code to the user."""
        subject = f"Your reservation for {event.name}"
        message = render_to_string('spark_bytes/email/qr_code_email.html', {
            'event': event,
            'qr_code_data': qr_code_data,
        })
        plain_message = strip_tags(message)

        email = EmailMessage(
            subject,
            plain_message,
            'ckraus99@gmail.com',  # From email (this can be the same as EMAIL_HOST_USER)
            [user_email],  # Recipient email
        )
        email.content_subtype = 'html'  # Email format: HTML
        email.attach('qr_code.png', qr_code_data, 'image/png')  # Attach QR code as image file
        email.send()


class CustomLoginView(LoginView):
    template_name = 'spark_bytes/login.html'
    authentication_form = CustomAuthenticationForm

    def get_success_url(self):
        return reverse_lazy('all_events')


class CustomLogoutView(LogoutView):
    next_page = 'login'

# Function-based view to delete an event
class DeleteEventView(UserPassesTestMixin, DetailView):
    model = Event
    template_name = "spark_bytes/event_detail.html"

    def test_func(self):
        return self.request.user.is_superuser  # Restrict to admin users

    def post(self, request, *args, **kwargs):
        event = self.get_object()
        event.delete()
        return JsonResponse({'message': 'Event deleted successfully!'}, status=200)
