# Generated by Django 3.1.12 on 2021-10-24 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cancelacion',
            old_name='id',
            new_name='ID',
        ),
        migrations.RenameField(
            model_name='reserva',
            old_name='id',
            new_name='ID',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='id',
            new_name='ID',
        ),
        migrations.RemoveField(
            model_name='cancelacion',
            name='message',
        ),
        migrations.AddField(
            model_name='cancelacion',
            name='code',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='cancelacion',
            name='descripcionCancelacion',
            field=models.CharField(max_length=500, null=True),
        ),
    ]