from django.db import models

class Page(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, null=True, blank=True,)

    def __str__(self):
        return self.name

class Picture(models.Model):
    image = models.ImageField(upload_to="pictures")
    text = models.CharField(max_length=200)
    page = models.ForeignKey(Page, null=True, blank=True, on_delete=models.SET_NULL, related_name="pictures")

    def __str__(self):
        return str(self.page) + " - " + self.text
        # return self.image.name