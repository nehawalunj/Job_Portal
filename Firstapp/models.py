from django.db import models


#thus is to fill mechanical job info
class MechanicalJobs(models.Model):
    company_name = models.CharField(max_length=50)
    job_title   = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    designation = models.CharField(max_length=20)
    experience = models.FloatField()
    package = models.FloatField()
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.company_name

#thus is to fill IT job info
class ItJobs(models.Model):
    company_name = models.CharField(max_length=50)
    job_title   =models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    designation = models.CharField(max_length=20)
    experience = models.FloatField()
    package = models.FloatField()
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.company_name

#this is to fill Civil job info
class CivilJobs(models.Model):
    company_name = models.CharField(max_length=50)
    job_title   =models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    designation = models.CharField(max_length=20)
    experience = models.FloatField()
    package = models.FloatField()
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.company_name
