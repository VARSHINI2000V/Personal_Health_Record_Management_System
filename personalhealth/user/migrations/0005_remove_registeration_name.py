# Generated by Django 3.2 on 2021-07-10 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20210625_1148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registeration',
            name='name',
        ),
    ]