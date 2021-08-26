# Generated by Django 2.2.24 on 2021-08-26 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectAbsen', '0006_auto_20210826_1643'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaksi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AbsensiIn', models.DateTimeField(auto_now_add=True)),
                ('AbsensiOut', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='jurusan',
            name='Jurusan',
            field=models.CharField(choices=[('TMPO', 'TMPO'), ('TTL', 'TTL'), ('TEDK', 'TEDK'), ('KGSP', 'KGSP'), ('SIJA', 'SIJA'), ('TFLM', 'TFLM')], max_length=10),
        ),
        migrations.AlterField(
            model_name='kelas',
            name='Kelas',
            field=models.CharField(choices=[('XII TEDK 1', 'XII TEDK 1'), ('XII TTL 2', 'XII TTL 2'), ('XII TMPO 1', 'XII TMPO 1'), ('XII TMPO 2', 'XII TMPO 2'), ('XII SIJA 1', 'XII SIJA 1'), ('XII TEDK 2', 'XII TEDK 2'), ('XII TTL 1', 'XII TTL 1'), ('XII SIJA 2', 'XII SIJA 2'), ('XII TFLM 2', 'XII TFLM 2'), ('XII KGPS 1', 'XII KGSP 1'), ('XII KGSP 2', 'XII KGSP 2'), ('XII TFLM 1', 'XII TFLM 1')], max_length=10, null=True),
        ),
    ]
