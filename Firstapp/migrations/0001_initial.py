# Generated by Django 3.0.7 on 2020-07-09 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=20)),
                ('phoneno', models.IntegerField(max_length=10)),
            ],
        ),
    ]
