# Generated by Django 5.0.1 on 2024-02-09 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entity',
            name='category',
        ),
        migrations.AddField(
            model_name='entity',
            name='category',
            field=models.ManyToManyField(related_name='categories', to='entities.category'),
        ),
    ]
