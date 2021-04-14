from django.db import models

# Create your models here.

class Media(models.Model):
    m_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=20)
    release_date = models.DateField()
    cover_art_url = models.CharField(max_length=200)

    class Meta:
        abstract = True



class Movie(Media):
    runningTime = models.CharField(max_length=30)
    director = models.CharField(max_length = 30)

    def __str__(self):
        return self.title


    
class TvShow(Media):
    seasons = models.IntegerField()
    episodeCount = models.IntegerField()

    def __str__(self):
        return self.title



class User(models.Model):
    userId = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    isAdmin = models.BooleanField()

    def __str__(self):
        return self.name



class Room(models.Model)
    roomId = models.IntegerField(primary_key=True)
    passcode = models.CharField(max_length = 16)
    hostId = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.roomId



class Review(models.Model)
    mediaId = models.ForeignKey(Media, on_delete = models.CASCADE)
    userId = models.ForeignKey(User, on_delete = models.CASCADE)
    rating = models.IntegerField()
    comment = models.CharField(max_length = 5000)

    def __str__(self):
        return self.comment



class Likes(models.Model)
    mediaId = models.ForeignKey(Media, on_delete = models.CASCADE)
    userId = models.ForeignKey(User, on_delete = models.CASCADE)



class Dislikes(models.Model)
    mediaId = models.ForeignKey(Media, on_delete = models.CASCADE)
    userId = models.ForeignKey(User, on_delete = models.CASCADE)



class Last_Showed(models.Model)
    mediaId = models.ForeignKey(Media, on_delete = models.CASCADE)
    userId = models.ForeignKey(User, on_delete = models.CASCADE)
    time = models.IntegerField()

    def __str__(self)
        return self.mediaId, self.time


class Suggested(models.Model)
    roomId = models.ForeignKey(Room, on_delete = models.CASCADE)
    mediaId = models.ForeignKey(Media, on_delete = models.CASCADE)
    time = models.IntegerField()

    def __str__(self)
        return self.mediaId



class Add(models.model)
    mediaId = models.ForeignKey(Media, on_delete = models.CASCADE)
    userId = models.ForeignKey(User, on_delete = models.CASCADE)
    time = models.IntegerField()

    def __str__(self)
        return self.mediaId



class Delete(models.model)
    mediaId = models.ForeignKey(Media, on_delete = models.CASCADE)
    userId = models.ForeignKey(User, on_delete = models.CASCADE)
    time = models.IntegerField()

    def __str__(self)
        return self.mediaId

    


    


    
