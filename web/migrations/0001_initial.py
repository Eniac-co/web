# Generated by Django 2.2.5 on 2020-01-15 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='clients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('location', models.CharField(default=None, max_length=50, null=True)),
                ('timezone', models.DateTimeField(default=None, null=True)),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='coders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.EmailField(max_length=50)),
                ('profilePic', models.ImageField(default=None, null=True, upload_to='profilePic')),
                ('intro', models.CharField(default=None, max_length=1000, null=True)),
                ('location', models.CharField(default=None, max_length=50, null=True)),
                ('timezone', models.DateTimeField(default=None, null=True)),
            ],
        ),
    ]
