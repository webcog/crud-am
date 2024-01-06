from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    father_name = models.CharField(max_length=50)
    roll_no = models.IntegerField()
    phone_no = models.IntegerField()
    postal_code = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.first_name)


