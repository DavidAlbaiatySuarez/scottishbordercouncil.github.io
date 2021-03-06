# Generated by Django 3.2.9 on 2022-01-08 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MultiStepFormModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('organisation', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('id_number', models.CharField(max_length=255)),
                ('box_1', models.CharField(max_length=500)),
                ('box_2', models.CharField(max_length=500)),
                ('box_3', models.CharField(max_length=500)),
                ('box_4', models.CharField(max_length=500)),
                ('box_5', models.CharField(max_length=500)),
                ('box_6', models.CharField(max_length=500)),
                ('box_7', models.CharField(max_length=500)),
                ('box_8', models.CharField(max_length=500)),
                ('box_9', models.CharField(max_length=500)),
            ],
        ),
    ]
