# Generated by Django 4.0.5 on 2022-06-11 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_alter_author_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
