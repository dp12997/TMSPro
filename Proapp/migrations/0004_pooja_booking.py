# Generated by Django 3.1.2 on 2021-03-23 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proapp', '0003_auto_20210315_0932'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pooja_booking',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=50)),
                ('mname', models.CharField(default='', max_length=50)),
                ('lname', models.CharField(default='', max_length=50)),
                ('address', models.TextField(default='')),
                ('emailid', models.EmailField(default='', max_length=50)),
                ('nopeople', models.IntegerField(default=0)),
                ('pdate', models.DateField()),
                ('ptime', models.TimeField()),
                ('pcategory', models.CharField(max_length=50)),
                ('city', models.CharField(default='', max_length=50)),
                ('zipcode', models.IntegerField(default=0)),
            ],
        ),
    ]