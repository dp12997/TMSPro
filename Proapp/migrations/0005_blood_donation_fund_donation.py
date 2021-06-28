# Generated by Django 3.1.2 on 2021-03-23 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proapp', '0004_pooja_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blood_donation',
            fields=[
                ('bid', models.AutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=50)),
                ('mname', models.CharField(default='', max_length=50)),
                ('lname', models.CharField(default='', max_length=50)),
                ('address', models.TextField(default='')),
                ('emailid', models.EmailField(default='', max_length=50)),
                ('mobileno', models.IntegerField(default=0)),
                ('bdate', models.DateField()),
                ('btime', models.TimeField()),
                ('bgroup', models.CharField(max_length=50)),
                ('city', models.CharField(default='', max_length=50)),
                ('zipcode', models.IntegerField(default=0)),
                ('feedback', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Fund_donation',
            fields=[
                ('fid', models.AutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=50)),
                ('mname', models.CharField(default='', max_length=50)),
                ('lname', models.CharField(default='', max_length=50)),
                ('address', models.TextField(default='')),
                ('emailid', models.EmailField(default='', max_length=50)),
                ('mobileno', models.IntegerField(default=0)),
                ('city', models.CharField(default='', max_length=50)),
                ('zipcode', models.IntegerField(default=0)),
                ('damount', models.IntegerField(default=0)),
            ],
        ),
    ]
