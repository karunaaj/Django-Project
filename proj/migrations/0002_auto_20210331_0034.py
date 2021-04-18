# Generated by Django 3.1.7 on 2021-03-30 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='id',
        ),
        migrations.RemoveField(
            model_name='statuslog',
            name='chamber_fid',
        ),
        migrations.AddField(
            model_name='account',
            name='uid',
            field=models.AutoField( primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='statuslog',
            name='log_fid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='log_checker', to='proj.datalog'),
        ),
        migrations.AddField(
            model_name='statuslog',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='datalog',
            name='log_id',
            field=models.AutoField( primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='statuslog',
            name='status_id',
            field=models.AutoField( primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(max_length=150, null=True)),
                ('resolved', models.BooleanField(null=True)),
                ('account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='account_owner', to='proj.account')),
            ],
        ),
    ]