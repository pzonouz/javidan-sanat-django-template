# Generated by Django 5.0.2 on 2024-02-11 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0003_remove_entity_category_entity_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specification',
            name='entities',
            field=models.ManyToManyField(related_name='specifications', to='entities.entity'),
        ),
    ]
