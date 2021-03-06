# Generated by Django 2.2.7 on 2020-02-26 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_userlog'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSignup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('phone_number', models.IntegerField()),
                ('address', models.CharField(max_length=25)),
                ('userlog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.UserLog')),
            ],
        ),
    ]
