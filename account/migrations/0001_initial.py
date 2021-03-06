# Generated by Django 2.2.5 on 2019-09-21 09:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique='true')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField(default=django.utils.timezone.now)),
                ('job_title', models.CharField(blank=True, max_length=50)),
                ('department', models.CharField(blank=True, max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('contact_number', models.CharField(blank=True, max_length=12)),
                ('status_is_active', models.BooleanField()),
                ('date_of_joining', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('-username',),
            },
        ),
    ]
