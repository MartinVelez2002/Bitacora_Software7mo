# Generated by Django 5.0 on 2024-01-02 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Docentes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='docentesmodel',
            name='telefono',
            field=models.IntegerField(default=0),
        ),
    ]
