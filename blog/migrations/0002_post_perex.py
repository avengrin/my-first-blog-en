# Generated by Django 4.1.7 on 2023-03-17 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='perex',
            field=models.TextField(blank=True, null=True),
        ),
    ]
