# from .models import Question
# from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.template import loader
from django.utils import timezone
from .models import Post
from django.shortcuts import redirect

# def index(request):

    # return HttpResponse("Hello, world. You're at the polls index.")
# def detail(request, question_id):
   # return HttpResponse("You're looking at question %s." % question_id)
# def results(request, question_id):

   # response = "You're looking at the results of question %s."
   # return HttpResponse(response % question_id)
# def vote(request, question_id):
 #  return HttpResponse("You're voting on question %s." % question_id)
# def index(request):
  #  latest_question_list = Question.objects.order_by('-pub_date')[:5]
  #  template = loader.get_template('polls/index.html')
  #  context = { 'latest_question_list': latest_question_list, }

    # return HttpResponse(template.render(context, request))

#Post.objects.get(pk=pk)
# ----------------------------------------//-------------------------------------------------------


def post_list(request):

      post = Post.objects.filter( published_date__lte=timezone.now()).order_by('published_date')
      return render(request, 'polls/postlist.html', {'post': post})

# ----------------------------------------//-------------------------------------------------------


def post_detail(request, pk):
     
     post = get_object_or_404(Post, pk=pk)
     return render(request, 'polls/post_detail.html', {'post': post})

# ----------------------------------------//-------------------------------------------------------


def post_new(request):


     if request.method == "POST":
         form = PostForm(request.POST)
         if form.is_valid():
             post = form.save(commit=False)
             post.author = request.user
             post.published_date = timezone.now()
             post.save()
             return redirect('post_detail', pk=post.pk)
     else:
         form = PostForm()
     return render(request, 'polls/post_edit.html', {'form': form})

   
        
# ----------------------------------------//-------------------------------------------------------

def post_edit(request, pk):
     post = get_object_or_404(Post, pk=pk)
     if request.method == "POST":
         form = PostForm(request.POST, instance=post)
         if form.is_valid():
             post = form.save(commit=False)
             post.author = request.user
             post.published_date = timezone.now()
             post.save()
             return redirect('post_detail', pk=post.pk)
     else:
         form = PostForm(instance=post)
     return render(request, 'polls/post_edit.html', {'form': form})
