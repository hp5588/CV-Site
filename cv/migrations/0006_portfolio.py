# Generated by Django 3.0.7 on 2020-08-22 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0005_skillcategory_collapse'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='portfolio/images')),
                ('description', models.TextField()),
                ('rank', models.IntegerField()),
            ],
        ),
    ]
