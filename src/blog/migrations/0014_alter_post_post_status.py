# Generated by Django 3.2.18 on 2023-04-03 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20230403_0251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_status',
            field=models.CharField(choices=[('draft', 'Draft'), ('publish', 'Published')], default='draft', max_length=50),
        ),
    ]
