# Generated by Django 4.1.5 on 2023-05-13 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('progressmeter', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'verbose_name_plural': 'Activities'},
        ),
        migrations.RenameField(
            model_name='task',
            old_name='reason',
            new_name='desc',
        ),
    ]
