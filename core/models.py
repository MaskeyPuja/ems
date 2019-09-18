from django.db import models

# Create your models here.
class Profile(models.Model):
	USER = (
		('Coordinator', 'Coordinator'),
		('Tasker', 'Tasker'),
	)
	user = models.CharField(max_length=15, choices=USER)
	name = models.CharField(max_length=50)
	address = models.CharField(max_length=150)

	def __str__(self):
		return self.name