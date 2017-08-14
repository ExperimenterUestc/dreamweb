from django.db import models
from UserManage.models import User

class Article(models.Model):
    name = models.CharField(max_length=64)
    text = models.TextField(max_length=10240)
    mod_date = models.DateTimeField(auto_now=True)
    author  = models.ForeignKey(User)
    def __unicode__(self):
        return self.name