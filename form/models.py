from django.db import models
from django.utils import timezone
		
class Member(models.Model):

       
       residing_state = models.CharField(max_length=50)
       residing_city = models.CharField(max_length=50)



class State(models.Model):

         state=models.CharField(max_length=20)
                

class City(models.Model):

        city=models.CharField(max_length=20)
        state=models.ForeignKey(State)
