# Generated by Django 3.0.1 on 2021-02-09 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20201028_1617'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quantitative',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500)),
                ('la', models.CharField(max_length=500)),
                ('lb', models.CharField(max_length=500)),
                ('lc', models.CharField(max_length=500)),
                ('ld', models.CharField(max_length=500)),
                ('ans', models.CharField(max_length=500)),
            ],
        ),
    ]
