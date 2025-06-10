from django.utils import timezone
from django.db import models
from django.forms import ValidationError
from accounts.models import CustomUser
from catalogue.models import Item

# Create your models here.
class Order(models.Model):
    id_Customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    id_Item = models.ForeignKey(Item, on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()
    price = models.IntegerField()
    address = models.TextField(default=None)
    slug = models.SlugField(unique=True)

    def clean(self):
        if(self.end <= self.start):
            raise ValidationError({ 'end': 'Дата и время окончания должно быть после времени начала'})
        if(self.end < timezone.now()):
            raise ValidationError({ 'end': 'Некорректное время'})
        if(self.start < timezone.now()):
            raise ValidationError({ 'start': 'Некорректное время'})
        super().clean()

    def __str__(self):
        return str(id)