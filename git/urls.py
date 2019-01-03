from django.urls import path
from .views import gitsearch,GitIndex

app_name = 'git'

urlpatterns = [
	path('all/',GitIndex.as_view(),name='q'),
	path('',gitsearch,name='search')
]