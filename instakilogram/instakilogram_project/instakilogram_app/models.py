from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images")
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
