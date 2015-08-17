from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Comment(models.Model):
	title = models.TextField(default='title')
	text = models.TextField()
	created = models.DateTimeField(default=datetime.now)
	user = models.ForeignKey(User)

	def __unicode__(self):
		return u"{0} at {1}".format(self.text, str(self.created))