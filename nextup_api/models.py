from django.db import models

# Create your models here.

class Media(models.Model):
    m_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=20)
    release_date = models.DateField()
    cover_art_url = models.CharField(max_length=200)

    def __str__(self):
        return self.title
