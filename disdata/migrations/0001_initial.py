# Generated by Django 3.0.7 on 2020-07-03 15:58

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease_name', models.CharField(max_length=1024)),
                ('mortality', models.FloatField()),
                ('morbidity', models.FloatField()),
                ('info_diagnostic', models.TextField()),
                ('info_managerial', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=1024)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(max_length=6)),
                ('phone_number', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=32)),
                ('located_at', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reported_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('reported_at', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('mortality', models.FloatField()),
                ('morbidity', models.FloatField()),
                ('infections', models.IntegerField()),
                ('disease', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='disdata.Disease')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=32)),
                ('located_at', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
