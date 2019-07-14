from django.db import models
from django.utils import timezone
from django.conf import settings

##------------------------------------------Django Girls Mode--------------------------------------------#
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(  default=timezone.now)
    published_date = models.DateTimeField( blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

##------------------------------------------Documentation--------------------------------------------#

#class Question(models.Model): 
    #question_text = models.CharField(max_length=200) 
    #pub_date = models.DateTimeField('date published')

#def __str__(self): 
    
   # return self.question_text

#class Choice(models.Model):

   #def __str__(self): 
       
      # return self.choice_text

    #question = models.ForeignKey(Question, on_delete=models.CASCADE) 
    #choice_text = models.CharField(max_length=200) 
    #votes = models.IntegerField(default=0)