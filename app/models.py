from django.db import models
from django.urls import reverse
class Post(models.Model):
    authors = (
        ("Shahzod","Shahzod"),
        ("Asilbek","Asilbek"),
        ("Abdullo","Abdullo"),
        ("Nurbek","Nurbek"),
        ("Bilolxo'ja","Bilolxo'ja"),
    )

    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=150)
    photo = models.ImageField(upload_to="static/img/")
    date = models.DateTimeField()
    authors = models.CharField(choices=authors, max_length=20)

    def _str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=10)
    email = models.EmailField(max_length=30)
    sms = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('contact')









# Create your models here.
