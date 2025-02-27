from django.db import models
from PIL import Image
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User



def validate_image_dimension(image):
    """دالة للتحقق من أبعاد الصورة قبل حفظها"""
    min_width = 100
    min_height = 50

    img = Image.open(image)
    width, height = img.size

    if width < min_width or height < min_height:
        raise ValidationError(f"Image should be at least {min_width}x{min_height} pixels.")


class BasePage(models.Model):
    Title = models.CharField(max_length=100)
    Sub_title = models.CharField(max_length=100, blank=True , null=True)
    bg_image = models.ImageField(upload_to= 'images/%Y/%m/%d/', validators=[validate_image_dimension],blank=True , null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.Title


class AboutPage(BasePage):
    Description = models.TextField(blank=True , null=True)

class ContactPage(BasePage):
    Description = models.TextField(blank=True , null=True)


class Post(models.Model):
    title = models.CharField(max_length=100)
    post_img = models.ImageField(upload_to='images/%Y/%m/%d/', validators=[validate_image_dimension] , blank=True , null=True)
    Sub_title = models.CharField(max_length=100,blank=True , null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title





class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created_at']
        indexes = [
            models.Index(fields=['created_at'])
        ]

    def __str__(self):
            return f"{self.name} - {self.content[:20]}"