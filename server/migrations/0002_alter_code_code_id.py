# Generated by Django 4.1.4 on 2022-12-20 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='code_id',
            field=models.CharField(default='na', max_length=6),
        ),
    ]
