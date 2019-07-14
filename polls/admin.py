#from .models import Question
from django.contrib import admin
from .models import Post


#------------------------------------------Django Girls Mode--------------------------------------------#

admin.site.register(Post)

##-----------------------------------------Documentation Mode---------------------------------------------#

#admin.site.register(Question) #registra uma aba de atividades no seu perfil de admin 
