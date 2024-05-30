from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name




class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', blank=True,null=True)

    def __str__(self):
        return f"{self.title} - {self.data} -{self.id}"


class LatestNews(models.Model):
    data = models.DateField(auto_now_add=True)
    text = models.TextField()

    def __str__(self):
        return f"{self.data} - {self.text}"


class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    image = models.ImageField(upload_to='profile_images/', blank=True,null=True)
    tel = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} "
