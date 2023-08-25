from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class poll(models.Model):
    question = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    pud_date = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.question
    

class choice(models.Model):
    poll = models.ForeignKey(poll, related_name="choices", on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)

    def __str__(self):
       return self.choice_text
    
class vote(models.Model):
    choice = models.ForeignKey(choice, related_name='votes', on_delete=models.CASCADE)
    poll =  models.ForeignKey(poll, on_delete=models.CASCADE)
    voted_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ["poll", "voted_by"]
   

