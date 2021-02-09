from django.utils import timezone
from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from TukeSchool.utils import unique_slug_generator
from django.db.models.signals import pre_save


class Events(models.Model):
    name = models.CharField(max_length=400)
    image = models.ImageField(upload_to='Events')
    date = models.DateTimeField(default=timezone.now)
    time = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    body = RichTextField()
    slug = models.SlugField(max_length=400, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('event_details', kwargs={"slug": self.slug})

    class Meta:
        ordering = ['-date']


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(slug_generator, sender = Events)
