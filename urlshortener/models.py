from django.db import models
from .utils import create_shortened_url

class Shortener(models.Model):
    """ 
    Creates a short url based on the long one
    created -> Hour and Date a shortener was created
    timer_followed -> Times the shortened link has benn followed
    long_url -> the original url link
    short_url -> shortened link
    """

    created = models.DateTimeField(auto_now_add=True)
    times_followed = models.PositiveIntegerField(default=0)
    long_url = models.URLField()
    short_url = models.CharField(max_length=15, unique=True, blank=True)
    
    class Meta:
        
        ordering = ["-created"]
        
    def __str__(self):
        
        return f'{self.long_url} to {self.short_url}'
    
    def save(self, *args, **kwargs):
        
        # if the short url wasn't specified
        if not self.short_url:
            self.short_url = create_shortened_url(self)
            
        super().save(*args, **kwargs)