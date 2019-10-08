from django.db import models

class Fibonacci(models.Model):
	duration = models.CharField(max_length=100, blank=True, null=True)
	input = models.PositiveIntegerField(blank=True, null=True)
	output = models.PositiveIntegerField(blank=True, null=True)
	
	def __str__(self):
		return self.output
