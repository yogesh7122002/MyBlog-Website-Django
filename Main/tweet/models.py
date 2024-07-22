# from django.db import models
# from django.contrib.auth.models import User

# # Create your models here.


# class Tweet(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     text = models.TextField(max_length=240,default="")
#     photo = models.ImageField(upload_to='photos/',blank=True,null=True)
#     created_time = models.DateTimeField(auto_now_add=True) 
#     updated_dt = models.DateTimeField(auto_now_add=True)
#     def __str__(self) :
#         return f'{self.user.username} - {self.text[:10]}'



from django.db import models
from django.contrib.auth.models import User

class Tweet(models.Model):
    heading  = models.TextField(default="")
    text = models.TextField(default="")
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text[:20]
