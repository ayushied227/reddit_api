from cgitb import text
from django.db import models
from reddit_api.models import User, BaseModel
from ckeditor.fields import RichTextField
# Create your models here.


class Tag(BaseModel):
    name = models.CharField(max_length=100)

class BasePost(BaseModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = RichTextField()
    media = models.TextField(null=True, blank=True)
    upvote_count = models.IntegerField(default=0)

class Question(BasePost):
    title = models.TextField()
    tags = models.ManyToManyField(Tag)
    
class Answer(BasePost):
    question_object = models.ForeignKey(Question, on_delete=models.CASCADE)
    this_worked = models.BooleanField(default=False)