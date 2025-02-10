# Generated by Django 5.1.5 on 2025-02-10 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('desc', models.CharField(max_length=200)),
                ('likes', models.PositiveIntegerField()),
                ('datetimePosted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
