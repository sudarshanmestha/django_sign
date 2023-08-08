from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import CustomUsercreationForm

# Create your views here.
def home(request):
    return render(request, 'index.html')


class SignupView(CreateView):
    form_class = CustomUsercreationForm
    success_url = '/accounts/login'
    template_name = 'registration/signup.html'

