from django.db import models
# third party apps
from model_utils.models import TimeStampedModel

# Create your models here.

class Home(TimeStampedModel):

    title = models.CharField(
        'Name', 
        max_length=50
    )
    description = models.TextField()
    about_title = models.CharField(
        'Our Title',
        max_length=50
    )
    about_text = models.TextField()
    contact_email = models.EmailField(
        'contact email',
        blank=True,
        null=True
    )
    phone = models.CharField(
        'Contact telephone', 
        max_length=25
    )

    class Meta:
        verbose_name = 'Principal Page'
        verbose_name_plural = 'Principal Page'

    def __str__(self):
        return self.title

class Subcriber(TimeStampedModel):

    email = models.EmailField()

    class Meta:
        verbose_name = 'subcriber'
        verbose_name_plural = 'subcribers'

    def __str__(self):
        return self.email

class Contact(TimeStampedModel):

    full_name = models.CharField(
        'Names', 
        max_length=60
    )
    email = models.EmailField()
    message = models.TextField()

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Messages'

    def __str__(self):
        return self.email