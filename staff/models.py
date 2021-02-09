from django.db import models
from TukeSchool.utils import unique_slug_generator
from django.db.models.signals import pre_save
from django.urls import reverse
from ckeditor.fields import RichTextField

category_choice = (('Teaching Staff', 'Teaching Staff'), ('Non-Teaching Staff', 'Non-Teaching Staff'))


class Staff(models.Model):
    name = models.CharField(max_length=400)
    image = models.ImageField(upload_to='staff')
    category = models.CharField(choices=category_choice, max_length=50)
    slug = models.SlugField(max_length=250, blank=True)
    description = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('staff_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['name']


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(slug_generator, sender=Staff)
