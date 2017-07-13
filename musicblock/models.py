# -*- coding: utf-8 -*-
from django.db import models 


# Create your models here. 


class Music(models.Model): 
	title = models.CharField(max_length=255, verbose_name='音樂名稱') 
	description = models.TextField(verbose_name='音樂敘述') 
	price = models.IntegerField(verbose_name='價格') 

	def __str__(self): 
		return self.title 

