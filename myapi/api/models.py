from django.db import models

# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.title, self.body)



class DataForm1(models.Model):
    _id = models.IntegerField(primary_key=True)
    event_date = models.CharField(max_length=30)
    start_time = models.CharField(max_length=30)
    stop_time = models.CharField(max_length=30)
    s_county = models.CharField(max_length=30)
    sub_county = models.CharField(max_length=30)
    s_village = models.CharField(max_length=30)
    area = models.CharField(max_length=30)
    s_activity = models.CharField(max_length=30)
    s_output = models.CharField(max_length=30)
    s_cost = models.CharField(max_length=30)
    facility_name = models.CharField(max_length=30)
    facility_type = models.CharField(max_length=30)
    lat = models.CharField(max_length=30)
    lon = models.CharField(max_length=30)
    officer_name = models.CharField(max_length=30)