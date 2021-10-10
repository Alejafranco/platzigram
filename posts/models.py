#Posts models

# Django
from django.contrib.auth.models import User
from django.db import models

#from users.models import Profile

#Todas las tablas son una clase en Django
# Post Model
class Post(models.Model):

    # Relacionarlo con un user
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts/photos')

    # Metadata
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    #Return title and username
    def __str__(self):
        return '{} by @{}'.format(self.title, self.user.username)
