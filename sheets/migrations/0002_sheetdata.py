# Generated by Django 3.2.3 on 2021-05-29 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SheetData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(max_length=10000)),
            ],
        ),
    ]
