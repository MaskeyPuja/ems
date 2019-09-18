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


class Task(models.Model):
	STATUS = (
		('started', 'Started'),
		('ongoing', 'Ongoing'),
		('completed', 'Completed'),
	)
	name = models.CharField(max_length=300)
	description = models.CharField(max_length=500)
	assigned_by = models.CharField(max_length=200)
	assigned_to = models.CharField(max_length=200)
	assigned_date = models.DateField()
	status = models.CharField(max_length=50, choices=STATUS)