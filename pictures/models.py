from django.db import models

class Page(models.Model):
    name = models.CharField(max_length=50)

    def pictures_path(instance, filename):
        return instance.id + '/' + filename

    picture1 = models.ImageField(upload_to="x")
    text1 = models.CharField(max_length=200)
    picture2 = models.ImageField(upload_to=pictures_path)
    text2 = models.CharField(max_length=200)
    picture3 = models.ImageField(upload_to=pictures_path)
    text3 = models.CharField(max_length=200)
    picture4 = models.ImageField(upload_to=pictures_path)
    text4 = models.CharField(max_length=200)

    def __str__(self):
        return self.name
        # return self.name