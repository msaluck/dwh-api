from django.db import models


class MasaStudi(models.Model):
    nim = models.CharField(max_length=9)
    nama = models.CharField(max_length=64)
    sks = models.IntegerField()
    ip = models.DecimalField(decimal_places=2, max_digits=5)
    masa_studi = models.FloatField()
    status = models.BooleanField()

    def __str__(self):
        return str(self.nim)


class KetepatanLulus(models.Model):
    nim = models.CharField(max_length=9)
    nama = models.CharField(max_length=64)

    def __str__(self):
        return str(self.nim)
