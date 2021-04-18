from django.db import models

# Create your models here.
class Account(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=50, blank=True)
    password = models.CharField(max_length=50, blank=True)
    contact = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.id.__str__() + " " + self.first_name.__str__() + " " + self.last_name.__str__() + " " + self.email.__str__() + " " + self.contact.__str__()

class DataLog(models.Model):
    id = models.AutoField(primary_key=True)
    pressure = models.FloatField()
    temperature = models.FloatField()
    dht_status = models.BooleanField(null=False)
    chamber_id = models.IntegerField()
    timestamp_log = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.id.__str__() + " " + self.pressure.__str__() + " " + self.temperature.__str__() + " " + self.dht_status.__str__() + " " + self.chamber_id.__str__() + " " + self.timestamp_log.__str__()


class StatusLog(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=50, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    log_fid = models.ForeignKey(DataLog,on_delete=models.CASCADE,related_name="log_checker",blank=True, null=True)

    def __str__(self):
        return self.id.__str__() + " " + self.status.__str__() + " " + self.timestamp.__str__() + " " + self.log_fid.__str__()

class Maintenance(models.Model):
    '''
        A Model class that has all the details of maintenance of the meter
        This is the table where maintenance info is stored.
        Any includes to be made to the maintence info should be made here
    '''
    #primary id of the maintenance info
    id = models.AutoField(primary_key=True)
    #date at which maintenance done
    date = models.DateTimeField(auto_now_add=True)
    #description of what kind of maintenance is done/problem is solved
    description = models.CharField(max_length=150,blank=False,null=True)
    #whether the problem is resolved or not
    resolved = models.BooleanField(blank=False,null=True)
    #account linked with the maintenance
    account = models.ForeignKey(Account,on_delete=models.SET_NULL,related_name="account_owner",blank=True,null=True)

    def __str__(self):
        return self.id.__str__() + " " + self.date.__str__() + " " + self.resolved.__str__() + " " + self.account.__str__()
