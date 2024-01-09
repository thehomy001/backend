from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Contact(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, validators=[RegexValidator(regex='^(\+?\d{1,3})?[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$')])
    message = models.TextField()