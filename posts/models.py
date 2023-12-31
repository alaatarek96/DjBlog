from django.db import models

''' 
        1 : html widget
        2 : validation 
        3 : best for db 
'''

# Create your models here.

''' 
    post :
        -title
        -content
        -draft
        -publish-date
        -author
        -image
        -tags
        -category
        -comments
'''

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=20000)
    draft = models.BooleanField(default=True)

    def __str__(self):
        return self.title