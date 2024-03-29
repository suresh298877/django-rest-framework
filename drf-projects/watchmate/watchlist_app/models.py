from django.db import models

# Create your models here.


class StreamPlatform(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=150)
    website = models.URLField(max_length=100)


class WatchList(models.Model):
    title = models.CharField(max_length=50)
    storyline = models.CharField(max_length=200)
    platform = models.ForeignKey(
        StreamPlatform, on_delete=models.CASCADE, related_name="watchlist")
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.title

# class Movie(models.Model):
#     name = models.CharField(max_length=50)
#     description = models.CharField(max_length=200)
#     active = models.BooleanField(default=True)

#     def __str__(self):
#         return self.name
