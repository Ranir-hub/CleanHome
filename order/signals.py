from django.dispatch import receiver 
from django.db.models import signals
from django.utils.crypto import get_random_string
from django.utils.text import slugify

from order.models import Order

@receiver(signals.pre_save, sender = Order)
def create_slug(sender, instance, **kwargs):
    slug_str = "%s %s" % (instance.id_Customer.username, get_random_string(length=4))
    instance.slug = slugify(slug_str)

    while Order.objects.filter(slug = instance.slug).exists():
        slug_str = "%s %s" % (instance.id_Customer.username, get_random_string(length=4))
        instance.slug = slugify(slug_str)
