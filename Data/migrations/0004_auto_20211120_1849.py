# Generated by Django 3.1.12 on 2021-11-20 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data', '0003_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
