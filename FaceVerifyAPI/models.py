from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length = 200)
    user_id = models.IntegerField()
    num_photos = models.IntegerField() 

class Face(models.Model):
    belongs_to = models.IntegerField()
    face_id = models.IntegerField()
    image_data = models.CharField(max_length = 5000000)
    embeddings = models.CharField(max_length = 10000)
