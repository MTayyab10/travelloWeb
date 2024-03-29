# Generated by Django 3.0.3 on 2020-03-23 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('details', models.TextField()),
                ('img', models.ImageField(upload_to='')),
                ('offer', models.BooleanField(default=False)),
            ],
        ),
    ]
