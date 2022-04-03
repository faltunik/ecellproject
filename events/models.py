from django.db import models
from PIL import Image

# Create your models here.

class Events(models.Model):
    name = models.CharField(max_length=100)
    venue = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    details = models.TextField()
    image = models.ImageField(upload_to= 'events/%Y/%m/%d', blank=True, null=True)
    email = models.EmailField()
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # taking some property from save method of this class and calling it
        if self.image:  # checking whther it has image or not
            img = Image.open(self.image)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)
