# Generated by Django 3.2 on 2021-05-27 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('mobile', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('dateofbirth', models.DateField()),
            ],
        ),
    ]
