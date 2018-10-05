# Generated by Django 2.0 on 2018-10-04 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0002_delete_stat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headNum', models.DecimalField(decimal_places=7, max_digits=50)),
                ('paraNum', models.DecimalField(decimal_places=7, max_digits=50)),
            ],
        ),
    ]
