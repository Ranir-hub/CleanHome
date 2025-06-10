from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()

    def __str__(self):
        return self.title
    
class Item(models.Model):
    id_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title  = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='images/')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title
    
    def snippet(self):
        return self.description[0:50] + '...'
    
