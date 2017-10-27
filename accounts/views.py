from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView as AuthLoginview
from django.http import JsonResponse
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required

class SignupFormView(CreateView):
	form_class = UserCreationForm
	template_name = 'accounts/signup_form.html'
	success_url = settings.LOGIN_URL

	def form_valid(self, form):
		response = super().form_valid(form)
		if self.request.is_ajax():
			return JsonResponse({'next_url': self.get_success_url()})
			#이렇게하면 서버에서 json응답을 받는다
		return response

	def get_template_names(self):
		if self.request.is_ajax():
			return ['accounts/_signup_form.html']
		return ['accounts/signup_form.html']
		#템플릿 구별 함수


class LoginView(AuthLoginview):
	def form_valid(self, form):
		response = super().form_valid(form)
		if self.request.is_ajax():
			return JsonResponse({'next_url': self.get_success_url()})
			#이렇게하면 서버에서 json응답을 받는다
		return response

	def get_template_names(self):
		if self.request.is_ajax():
			return ['accounts/_login.html']
		return ['accounts/login.html']
		#템플릿 구별 함수

@login_required
def profile(request):
	return render(request,'accounts/profile.html')