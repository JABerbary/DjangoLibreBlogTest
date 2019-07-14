from django.urls import path
from . import views

#--------------------------------------- Django Girls mode ---------------------------------------------#
urlpatterns = [

   path('', views.post_list, name='post_list'),
   path('post/<int:pk>/', views.post_detail, name='post_detail'),
   path('post/new/', views.post_new, name='post_new'),
   path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
   
  ]
#--------------------------------------- Documentation mode ---------------------------------------------#

    #path('', views.index, name='index'), 
     #ex: /polls/5/ 
    # path('<int:question_id>/', views.detail, name='detail'), 
     # ex: /polls/5/results/ 
    # path('<int:question_id>/results/', views.results, name='results'), 
      # ex: /polls/5/vote/ 
    # path('<int:question_id>/vote/', views.vote, name='vote'),
     #path('<int:question_id>/vote/', views.vote, name='vote'),

  

     
