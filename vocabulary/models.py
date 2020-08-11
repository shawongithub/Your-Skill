from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Vocabulary(models.Model):
    word = models.CharField(max_length=264, verbose_name="Put a Word")
    meaning=models.CharField(max_length=264, verbose_name="Meaning")
    word_image = models.ImageField(upload_to='images', verbose_name="Image")
    publish_date = models.DateTimeField(auto_now_add=True)
    google=models.URLField(max_length=264)
  
    class Meta:
        ordering = ['-publish_date',]

    def __str__(self):
        return self.word
class MyList(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, related_name='mylist')
    vocab=models.ForeignKey(Vocabulary, on_delete=models.CASCADE, related_name='vocabulary')

    def __str__(self):
        return self.user.username
   
class Comment(models.Model):
    word = models.ForeignKey(Vocabulary, on_delete=models.CASCADE, related_name='word_comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-comment_date',)
        
    def __str__(self):
        return self.comment



