from django.shortcuts import render,redirect

# Create your views here.
from .forms import GitForm
from .models import GitUser
from django.views.generic import ListView
import requests

class GitIndex(ListView):
	model = GitUser
	template_name = 'index.html'

	def get_context_data(self,**kwargs):

		global url , github_user

		github_user_query = GitUser.objects.all().last()
		github_user = github_user_query.search_query

		user_profile = requests.get('https://api.github.com/users/{}'.format(str(github_user)))
		user_repos = requests.get('https://api.github.com/users/{}/repos'.format(str(github_user)))
		detail_user_profile = requests.get('https://api.github.com/users/{}/repos'.format(str(github_user)))
		context  =dict()
		context['user'] = user_profile.json()
		context['repos'] = user_repos.json()
		context['detail_user_profile'] = detail_user_profile.json()
		return context

def gitsearch(requests):
	form = GitForm(requests.POST or None)
	if form.is_valid():
		form.save(commit=False)
		form.save()
		return redirect('git:q')
	context = {
		'form':form 
	}
	return render(requests,'base.html',context)
