from django.db import models

# Create your models here.
class SlackPerson(models.Model):
    slackUsername = models.CharField(max_length=100)
    backend = models.BooleanField(default=False)
    age = models.IntegerField()
    bio = models.TextField()

    def __str__(self):
        return self.slackUsername

# class MathOperate(models.Model):
#     operation_type = models.CharField(max_length=100)
#     x = models.IntegerField()
#     y = models.IntegerField()