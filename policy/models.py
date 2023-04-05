from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from datetime import datetime

choose = (
    ("social", "social"),
    ("sciTech", "sciTech"),
    ("environment", "environment"),
    ("foreign", "foreign"),
    ("economic", "economic"),
    ("other", "other"),
)
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete = models.CASCADE)
    image = models.ImageField(upload_to='images/', null=True,blank=True,default='default.jpg')
    image2 = models.ImageField(upload_to='images12/', null=True,blank=True,default='default.jpg')

    category = models.CharField(
        max_length = 20,
        choices = choose,
        )


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs = {'pk':self.pk} )
    
    class Meta:
        ordering = ['-date_posted']

    def datepublished(self):
        return self.date_posted.strftime('%B %d %Y')
    
    def get_date(self):
          time = datetime.now()
          if self.date_posted.day == time.day:
              return str(time.hour - self.date_posted.hour) +" hours ago"
          else:
              if self.date_posted.month == time.month:
                   return str(time.day - self.date_posted.day) + " days ago"

          return self.date_posted
   