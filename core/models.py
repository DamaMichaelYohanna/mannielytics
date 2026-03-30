from django.db import models
from cloudinary_storage.storage import MediaCloudinaryStorage



class Message(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return f"Message from {self.name} <{self.email}>"


class TeamMember(models.Model):
    """Model for team members/staff profiles"""
    name = models.CharField(max_length=200, help_text="Full name of the team member")
    title = models.CharField(max_length=300, help_text="Job title/position (e.g., CEO & Founder • System Engineer)")
    bio = models.TextField(help_text="Biography/description of the team member")
    image = models.ImageField(upload_to='team/', help_text="Profile photo of team member", storage=MediaCloudinaryStorage())
    
    # Optional links
    linkedin_url = models.URLField(max_length=500, blank=True, null=True, help_text="LinkedIn profile URL")
    portfolio_url = models.URLField(max_length=500, blank=True, null=True, help_text="Portfolio website URL")
    website_url = models.URLField(max_length=500, blank=True, null=True, help_text="Personal website URL")
    cv_url = models.URLField(max_length=500, blank=True, null=True, help_text="CV/Resume URL")
    
    # Ordering and status
    order = models.IntegerField(default=0, help_text="Display order (lower numbers appear first)")
    is_active = models.BooleanField(default=True, help_text="Whether to display this team member")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'Team Member'
        verbose_name_plural = 'Team Members'

    def __str__(self) -> str:
        return f"{self.name} - {self.title}"


class ConsultancyService(models.Model):
    """Model for services offered by the consultancy"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon_svg = models.TextField(help_text="Raw SVG path or heroicon name", blank=True)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'title']
        verbose_name = 'Consultancy Service'
        verbose_name_plural = 'Consultancy Services'

    def __str__(self) -> str:
        return self.title


class ConsultingProject(models.Model):
    """Model for projects completed by the consultancy"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    client = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='projects/', storage=MediaCloudinaryStorage())
    link = models.URLField(blank=True, help_text="Link to the project or case study")
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    completed_at = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-completed_at', 'order']
        verbose_name = 'Consulting Project'
        verbose_name_plural = 'Consulting Projects'

    def __str__(self) -> str:
        return self.title
