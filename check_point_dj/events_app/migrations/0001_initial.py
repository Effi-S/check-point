# Generated by Django 4.0.4 on 2022-05-19 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.TextField()),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
