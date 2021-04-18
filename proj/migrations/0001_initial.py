# Generated by Django 3.1.7 on 2021-03-17 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('password', models.CharField(blank=True, max_length=50)),
                ('contact', models.CharField(blank=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='DataLog',
            fields=[
                ('log_id', models.AutoField(primary_key=True, serialize=False)),
                ('pressure', models.FloatField()),
                ('temperature', models.FloatField()),
                ('dht_status', models.BooleanField()),
                ('chamber_id', models.IntegerField()),
                ('timestamp_log', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='StatusLog',
            fields=[
                ('status_id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(blank=True, max_length=50)),
                ('chamber_fid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proj.datalog')),
            ],
        ),
    ]
