from django.db import models
from django.core import validators
from django.core.validators import MaxValueValidator
from django.utils import timezone


# Create your models here.
class Jurusan(models.Model):

    Data_Jurusan = {('SIJA','SIJA'),
                    ('TMPO','TMPO'),
                    ('TFLM','TFLM'),
                    ('TEDK','TEDK'),
                    ('TTL','TTL'),
                    ('KGSP','KGSP')}

    id = models.PositiveIntegerField(primary_key=True, validators = [MaxValueValidator(999999999)])
    Jurusan = models.CharField(max_length=10, choices=Data_Jurusan)

    def __str__(self):
        return '{}.{}'.format(self.id, self.Jurusan)

class Siswa(models.Model):

    Gender = [('Pria','Pria'),
              ('Wanita','Wanita')]

    NISN = models.PositiveIntegerField(primary_key=True, validators = [MaxValueValidator(9999999999)])
    Nama = models.CharField(max_length=100)
    Jenis_Kelamin = models.CharField(max_length=10, choices=Gender)
    Alamat = models.CharField(max_length=50,null=True)
    id_kelas = models.PositiveIntegerField(validators = [MaxValueValidator(9999999999)])
    id_jurusan = models.PositiveIntegerField(validators = [MaxValueValidator(999999999)])
    id_transaksi = models.PositiveIntegerField(validators = [MaxValueValidator(9999999999)])
    AbsensiIn = models.DateTimeField(auto_now_add=True)
    AbsensiOut = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}.{}'.format(self.NISN,self.Nama)

class Kelas(models.Model):

    Data_Kelas = {('XII SIJA 1','XII SIJA 1'),
                  ('XII SIJA 2','XII SIJA 2'),
                  ('XII TMPO 1','XII TMPO 1'),
                  ('XII TMPO 2','XII TMPO 2'),
                  ('XII TFLM 1','XII TFLM 1'),
                  ('XII TFLM 2','XII TFLM 2'),
                  ('XII TEDK 1','XII TEDK 1'),
                  ('XII TEDK 2','XII TEDK 2'),
                  ('XII TTL 1','XII TTL 1'),
                  ('XII TTL 2','XII TTL 2'),
                  ('XII KGPS 1','XII KGSP 1'),
                  ('XII KGSP 2','XII KGSP 2')}

    id = models.PositiveIntegerField(primary_key=True, validators = [MaxValueValidator(9999999999)])
    Kelas = models.CharField(max_length=10, choices=Data_Kelas, null=True)

    def __str__(self):
        return '{}.{}'.format(self.id, self.Kelas)


class Transaksi(models.Model):
    id = models.PositiveIntegerField(primary_key=True, validators = [MaxValueValidator(9999999999)])
    AbsensiIn = models.DateTimeField(auto_now_add=True)
    AbsensiOut = models.DateTimeField(auto_now=True)
