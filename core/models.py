from django.db import models

# Create your models here.
class Profile(models.Model):
	USER = (
		('C', 'Coordinator'),
		('T', 'Tasker'),
	)
	user = models.CharField(max_length=2, choices=USER)
	name = models.CharField(max_length=50)
	address = models.CharField(max_length=150)

	def __str__(self):
		return self.name