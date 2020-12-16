from django.db import models


class Post(models.Model):
    author = models.CharField(max_length=120)
    title = models.CharField(max_length=120)
    text = models.TextField()
    password = models.CharField(max_length=120)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'post'

    def __str__(self):
        return self.title
