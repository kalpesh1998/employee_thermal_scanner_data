# Generated by Django 3.0.6 on 2020-06-16 01:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Temp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateField(auto_now=True)),
                ('temp_reading', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Temp_dev',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField(max_length=100)),
                ('temperature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.Temp')),
            ],
            options={
                'ordering': ['first_name'],
            },
        ),
    ]