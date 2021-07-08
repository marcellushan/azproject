# Generated by Django 2.1.5 on 2021-07-07 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('athletes', '0005_auto_20210707_1350'),
    ]

    operations = [
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='athlete',
            name='years',
            field=models.ManyToManyField(to='athletes.Year'),
        ),
    ]