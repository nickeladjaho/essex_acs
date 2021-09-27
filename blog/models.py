from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Author(models.Model):
    posted_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE, )
    full_name = models.CharField(primary_key=True, max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Orders data table by publication dates
        ordering = ['full_name']

    def __str__(self):
        # Outputs string of model object.
        return self.full_name


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True)
    additional_authors = models.CharField(blank=True, max_length=50,
                                          help_text='This field is optional')
    title = models.CharField(max_length=255)
    slug = models.SlugField(null=False, unique=True)
    tagline = models.CharField(max_length=80, blank=True)
    summary = models.TextField()
    published_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True, null=True, blank=True)
    photo = models.ImageField(upload_to='uploads/', blank=True)
    blog_content_file = models.FileField(upload_to='uploads/', blank=True)

    class Meta:
        ordering = ['published_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})
