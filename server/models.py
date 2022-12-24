from django.db import models

# Create your models here.
class Server(models.Model):
    server_id = models.CharField(max_length=10, primary_key=True)
    secret_key = models.CharField(max_length=20)

class Code(models.Model):
    server_id = models.CharField(max_length=10)
    code_id = models.CharField(max_length=6, default='na')
    title = models.CharField(max_length=60)
    code = models.TextField()