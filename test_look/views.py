from django.shortcuts import render
from models import Comment
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.

def index(request):
	comments = Comment.objects.all()
	return render(request,
		          'index.html',
		          {'comments':comments})

def sub_comment(request):
	comment = request.POST.get('comment')
	Comment.objects.create(Comment=comment)
	return HttpResponseRedirect('/')

def delete_comment(request, comment_id):
	Comment.objects.get(id=comment_id).delete()
	return HttpResponse('hello world')

def update_comment(request, comment_id):
	comment = request.POST.get('comment')
	Comment.objects.filter(id=comment_id).update(Comment=comment)
	# stats = Comment.objects.get(id=comment_id).stats
	# if stats :
	# 	Comment.objects.filter(id=comment_id).update(stats=False)
	# else:
	# 	Comment.objects.filter(id=comment_id).update(stats=True)



	return HttpResponseRedirect('/')