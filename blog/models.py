from django.db import models
from ckeditor.fields import RichTextField

class Blog(models.Model):
    description = RichTextField(config_name='extends')

    title = models.CharField(max_length=100, verbose_name='Sarlavha:')

    image = models.ImageField(upload_to='blog/', verbose_name='Rasm:', blank=True, null=True)  # new required
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    @property
    def get_image_url(self):
        if not self.image:
            url = ''
        else:
            url = self.image.url
        return url

    class Meta:
        ordering = ['-created_at']

# terminal
# python manage.py makemigrations
# python manage.py migrate

# CREATE TABLE Blog (
# id integer AUTOINCREMENT NOT NULL,
# title TEXT,
# description TEXT
# PRIMARY KEY(id));