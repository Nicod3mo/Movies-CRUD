from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey('auth.User', related_name='movies', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + " " + self.title

    class Meta:
        ordering = ['-id']