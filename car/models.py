from django.db import models


class Car(models.Model):

    idCarro = models.IntegerField(primary_key=True, db_column='ID')
    modeloCarro = models.CharField(max_length=50, db_column='MODELO')
    marcaCarro = models.CharField(max_length=50, db_column='MARCA')
    anoCarro = models.IntegerField(db_column='ANO')

    class Meta:
        managed=False
        db_table = 'car'
        app_label='car'

