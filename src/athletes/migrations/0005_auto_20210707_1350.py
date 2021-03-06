# Generated by Django 2.1.5 on 2021-07-07 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('athletes', '0004_auto_20210707_1250'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='athlete',
            name='schools',
            field=models.ManyToManyField(to='athletes.School'),
        ),
    ]
