# Generated by Django 2.2.16 on 2020-11-12 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0005_teacher_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='pointa',
            new_name='points',
        ),
        migrations.AddField(
            model_name='teacher',
            name='teacher_age',
            field=models.IntegerField(default=25, verbose_name='年龄'),
        ),
    ]
