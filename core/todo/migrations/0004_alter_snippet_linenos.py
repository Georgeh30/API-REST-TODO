# Generated by Django 4.1.1 on 2022-09-27 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_alter_snippet_linenos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='linenos',
            field=models.BooleanField(default=False),
        ),
    ]
