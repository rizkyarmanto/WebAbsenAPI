# Generated by Django 2.2.24 on 2021-08-26 09:54

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projectAbsen', '0007_auto_20210826_1649'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='siswa',
            name='absenIn',
        ),
        migrations.RemoveField(
            model_name='siswa',
            name='absenOut',
        ),
        migrations.AddField(
            model_name='siswa',
            name='id_transaksi',
            field=models.PositiveIntegerField(default=django.utils.timezone.now, validators=[django.core.validators.MaxValueValidator(9999999999)]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='jurusan',
            name='Jurusan',
            field=models.CharField(choices=[('TFLM', 'TFLM'), ('TMPO', 'TMPO'), ('SIJA', 'SIJA'), ('TTL', 'TTL'), ('TEDK', 'TEDK'), ('KGSP', 'KGSP')], max_length=10),
        ),
        migrations.AlterField(
            model_name='kelas',
            name='Kelas',
            field=models.CharField(choices=[('XII TEDK 2', 'XII TEDK 2'), ('XII KGSP 2', 'XII KGSP 2'), ('XII TMPO 1', 'XII TMPO 1'), ('XII TEDK 1', 'XII TEDK 1'), ('XII TFLM 1', 'XII TFLM 1'), ('XII TMPO 2', 'XII TMPO 2'), ('XII TTL 1', 'XII TTL 1'), ('XII SIJA 2', 'XII SIJA 2'), ('XII TFLM 2', 'XII TFLM 2'), ('XII TTL 2', 'XII TTL 2'), ('XII SIJA 1', 'XII SIJA 1'), ('XII KGPS 1', 'XII KGSP 1')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='transaksi',
            name='id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(9999999999)]),
        ),
    ]
