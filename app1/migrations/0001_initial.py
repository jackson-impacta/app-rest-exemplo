# Generated by Django 3.0.8 on 2020-07-13 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(blank=True, default=None, editable=False, null=True)),
                ('name', models.CharField(default='', max_length=255, verbose_name='Job Name')),
                ('address', models.CharField(default='', max_length=255, verbose_name='Address')),
                ('state', models.IntegerField(choices=[(1, 'AM'), (2, 'ES'), (3, 'MG'), (4, 'BH'), (5, 'RO')])),
                ('number', models.CharField(default='', max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(blank=True, default=None, editable=False, null=True)),
                ('name', models.CharField(default='', max_length=255, verbose_name='Task Name')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Job', verbose_name='Job')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
