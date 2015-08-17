from django.contrib import auth
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from gl_login.models import Comment

@login_required
def index(request):
	''' Comments view ''' 

	# Receiving a posted comment 
	if request.is_ajax() and request.method == 'GET':
		comment = request.GET.get('comment')
		title = request.GET.get('title')
		if comment:
			commentObj = Comment(title=title, text=comment, user=request.user)
			commentObj.save()
		return HttpResponse()

	# Otherwise just display all the comments from the db 
	context = {'comments': Comment.objects.all()}
	return render(request, 'index.html', context)

@login_required
def bye(request):
	''' Log out and show user goodbye page ''' 
	auth.logout(request)
	return render(request, 'bye.html')

