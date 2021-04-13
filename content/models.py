from django.db import models
from accounts.models import CustomUser
from django.core.validators import FileExtensionValidator


class Content(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    introduction = models.TextField()
    urls = models.URLField(blank=True)
    upload = models.FileField(
        upload_to='files/',
        validators=[FileExtensionValidator(['mp4'])]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    views_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title +'by'+ self.owner.username

class Comment(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    comment = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.owner.username + 'comment' + self.content.title


class Good(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)

    def __str__(self):
        return self.owner.username + 'good' + self.content.title
