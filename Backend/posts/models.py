from django.db import models

# Create your models here.

class Stat(models.Model):
	headNum= models.DecimalField(max_digits=50,decimal_places=7)
	paraNum= models.DecimalField(max_digits=50,decimal_places=7)

	# def __init__(self,headNum,paraNum):
	# 	self.headNum=headNum
	# 	self.paraNum=paraNum
		
	def __unicode__(self):
		return "{0} {1}".format(self, self.headNum, self.paraNum)

	def show(self):
		print(self.headNum)
		print(self.paraNum)