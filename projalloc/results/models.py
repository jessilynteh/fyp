from django.db import models

class Students(models.Model):
    student_id = models.IntegerField
    student_name = models.CharField(max_length=200)
    grade = models.FloatField()
    rank = models.IntegerField
    selection1 = models.CharField(max_length=200)
    selection2 = models.CharField(max_length=200)
    selection3 = models.CharField(max_length=200)
    selection4 = models.CharField(max_length=200)
    selection5 = models.CharField(max_length=200)

    def __str__(self):
        return self.student_name
