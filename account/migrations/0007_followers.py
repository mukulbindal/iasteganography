# Generated by Django 2.2.5 on 2019-09-22 10:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20190921_1841'),
    ]

    operations = [
        migrations.CreateModel(
            name='Followers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_when_followed', models.DateTimeField(default=django.utils.timezone.now)),
                ('user1', models.ForeignKey(on_delete=None, related_name='followes', to='account.Users')),
                ('user2', models.ForeignKey(on_delete=None, related_name='followed', to='account.Users')),
            ],
            options={
                'ordering': ('-user1',),
            },
        ),
    ]