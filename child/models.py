from django.db import models

class Collegeinfo(models.Model):
    cid = models.CharField(primary_key=True, max_length=12)
    cname = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'collegeinfo'

class Majorinfo(models.Model):
    mid = models.CharField(primary_key=True, max_length=12)
    cid = models.ForeignKey(Collegeinfo, models.DO_NOTHING, db_column='cid', blank=True, null=True)
    mname = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'majorinfo'

class Classinfo(models.Model):
    cid = models.CharField(primary_key=True, max_length=12)
    mid = models.ForeignKey('Majorinfo', models.DO_NOTHING, db_column='mid', blank=True, null=True)
    cname = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'classinfo'

class Card(models.Model):
    cardno = models.CharField(primary_key=True, max_length=12)
    sno = models.ForeignKey('Studentinfo', models.DO_NOTHING, db_column='sno', blank=True, null=True)
    cardmoney = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    cardtime = models.DateField()
    carpassword = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'card'


class Studentinfo(models.Model):
    sno = models.CharField(primary_key=True, max_length=12)
    sname = models.CharField(max_length=8)
    ssex = models.CharField(max_length=4, blank=True, null=True)
    sage = models.DateField()
    sdept = models.ForeignKey(Collegeinfo, models.DO_NOTHING, db_column='sdept', blank=True, null=True)
    sspecial = models.ForeignKey(Majorinfo, models.DO_NOTHING, db_column='sspecial', blank=True, null=True)
    sclass = models.ForeignKey(Classinfo, models.DO_NOTHING, db_column='sclass', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'studentinfo'

class Costinfo(models.Model):
    cnumber = models.CharField(primary_key=True, max_length=12)
    ctime = models.DateField()
    ccardno = models.ForeignKey(Card, models.DO_NOTHING, db_column='ccardno', blank=True, null=True)
    ccost = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'costinfo'

class Fillinfo(models.Model):
    rnumber = models.CharField(primary_key=True, max_length=12)
    rtime = models.DateField()
    rcardno = models.ForeignKey(Card, models.DO_NOTHING, db_column='rcardno', blank=True, null=True)
    rmoney = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fillinfo'

class Losinfo(models.Model):
    cardno = models.ForeignKey(Card, models.DO_NOTHING, db_column='cardno', primary_key=True)
    ltime = models.DateField()

    class Meta:
        managed = False
        db_table = 'losinfo'