# Generated by Django 3.2 on 2021-06-25 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_emergency_speciality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myrecord',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='myrecord',
            name='prescription',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
