from django.db import models
from django.contrib.auth.models import AbstractUser


# as described in the Django docs: https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#substituting-a-custom-user-model
# option #4 from https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#abstractuser

class User(AbstractUser):
    pass