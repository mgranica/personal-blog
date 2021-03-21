from django.db import models
from django.conf import settings
# third party apps
from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField
from .managers import EntryManager

# Create your models here.
class Category(TimeStampedModel):
    """ Categoria de entrada"""

    short_name = models.CharField(
        'Name', 
        max_length=50
    )
    name = models.CharField(
        'Name', 
        max_length=50
    )

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Tag(TimeStampedModel):

    name = models.CharField(
        'Name', 
        max_length=30
    )

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.name

class Entry(TimeStampedModel):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    tag = models.ManyToManyField(Tag)
    title = models.CharField(
        'Title', 
        max_length=50
    )
    summary = models.TextField('Summary')
    content = RichTextUploadingField('Content')
    public = models.BooleanField(default=False)
    image = models.ImageField(
        'Image',
        upload_to = 'Entry'
    )
    cover = models.BooleanField(default=False)
    in_home= models.BooleanField(default=False)
    slug = models.SlugField(editable=False, max_length=300)

    objects= EntryManager()
    
    class Meta:
        verbose_name = 'Entry'
        verbose_name_plural = 'Entries'

    def __str__(self):
        return self.title
