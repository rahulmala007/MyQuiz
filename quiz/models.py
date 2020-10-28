from django.db import models

# Create your models here.

class quiz(models.Model):
    title=models.CharField(max_length=20,blank=False)
    description=models.CharField(max_length=100)
    number_of_questions=models.IntegerField(default=0)
    random_order_required=models.BooleanField(default=False)
    start_date=models.DateField(blank=False,null=True)
    start_time=models.TimeField(blank=False,null=True)
    end_date=models.DateField(blank=False,null=True)
    end_time=models.TimeField(blank=False,null=True)
    duration=models.IntegerField(blank=False)

    def get_absolute_url(self):
        return f"/quiz/{self.id}"
    


