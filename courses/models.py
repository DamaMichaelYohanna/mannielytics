from django.db import models
from django.utils import timezone
from cloudinary_storage.storage import MediaCloudinaryStorage

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    short_description = models.CharField(max_length=300, blank=True)
    image = models.ImageField(upload_to='course_images/', blank=True, null=True,  storage=MediaCloudinaryStorage())  # Explicitly set the storage)
    features = models.TextField(help_text="Enter features separated by new lines", blank=True, null=True)
    duration = models.CharField(max_length=100, help_text="e.g., 3 months, 6 weeks", blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True)
    certification = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
    def get_features_list(self):
        """Convert features text to list for template rendering"""
        return [feature.strip() for feature in self.features.split('\n') if feature.strip()]
