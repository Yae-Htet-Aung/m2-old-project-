# Generated by Django 2.2 on 2023-09-11 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('total_employees', models.CharField(default=None, max_length=20, verbose_name='Total Employees')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(default='draft', max_length=10, verbose_name='Status')),
                ('is_active', models.BooleanField(default=False, verbose_name='Is Active')),
                ('address', models.CharField(blank=True, default='Yankin Township, Myanmanr Center', max_length=255, null=True)),
                ('city', models.CharField(blank=True, default='Yangon', max_length=100, null=True)),
                ('state', models.CharField(blank=True, default='Yangon Division', max_length=100, null=True)),
                ('postal_code', models.CharField(blank=True, default='11081', max_length=20, null=True)),
                ('country', models.CharField(blank=True, default='Myanmar', max_length=100, null=True)),
                ('phone', models.CharField(blank=True, default='09111000111', max_length=20, null=True)),
                ('email', models.EmailField(blank=True, default='dept@gmail.com', max_length=255, null=True)),
                ('budget', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True)),
                ('custom_field', models.TextField(blank=True, null=True)),
            ],
        ),
    ]