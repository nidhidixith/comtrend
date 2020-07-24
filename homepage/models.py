from django.db import models


class firsttable(models.Model):
    name=models.CharField(max_length=255)
    genre=models.CharField(max_length=100)
    link=models.CharField(max_length=500)


class byindians(models.Model):
    title=models.CharField(max_length=800)
    published_at=models.CharField(max_length=30)
    duration=models.CharField(max_length=30)
    description=models.CharField(max_length=500)
    channel=models.CharField(max_length=200)
    view_count=models.IntegerField()
    like_count=models.IntegerField()
    dislike_count = models.IntegerField()
    favorite_count=models.IntegerField()
    comment_count=models.IntegerField()
    language=models.CharField(max_length=50)
    tags=models.CharField(max_length=800)
    categories=models.CharField(max_length=800)
    type= models.CharField(max_length=300,default="")
    video_id=models.CharField(primary_key=True,max_length=255)






