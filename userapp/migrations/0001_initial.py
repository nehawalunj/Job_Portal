# Generated by Django 3.0.7 on 2020-07-13 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('confirm_password', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('contact', models.CharField(max_length=40)),
                ('resume', models.FileField(upload_to='files')),
            ],
        ),
    ]
