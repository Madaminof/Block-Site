from django.db import models
from django.contrib.auth.models import AbstractUser





class CreateUser(AbstractUser):
    image = models.ImageField(upload_to='user_image/', blank=True, null=True)
    from django.db import models



    class Meta:
        db_table = 'create_user'



    def __str__(self):
        return self.username



