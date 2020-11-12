# Generated by Django 2.2.16 on 2020-11-06 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_courseorg_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courseorg',
            old_name='fav_name',
            new_name='fav_nums',
        ),
        migrations.AlterField(
            model_name='courseorg',
            name='image',
            field=models.ImageField(upload_to='org/%Y/%m', verbose_name='封面图'),
        ),
    ]
