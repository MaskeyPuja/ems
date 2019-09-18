from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, CreateView, ListView, UpdateView
# from django.core.urlresolvers import reverse
# from django.utils.functional import lazy

from django.urls import reverse_lazy, reverse


from .models import Profile
from .form import ProfileForm
# Create your views here.

def indexView(request):
	return render(request, 'core/index.html')

@login_required
def dashboardView(request):
	return render(request, 'core/dashboard.html')

def registerView(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			print('hello')
			form.save()

			return redirect('login_url')
	else:
		form = UserCreationForm()	

	return render(request, 'registration/register.html', {'form': form})


class ProfileListView(ListView):
	model = Profile
	template_name = 'core/profile-list.html'


class ProfileCreateView(CreateView):
	model = Profile
	form_class = ProfileForm
	template_name = 'core/profile-form.html'

	success_url = reverse_lazy('profile_list')


class ProfileUpdateView(UpdateView):
	model = Profile
	form_class = ProfileForm
	template_name = 'core/profile-form.html'

	success_url = reverse_lazy('profile_list')

