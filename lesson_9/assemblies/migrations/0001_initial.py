# Generated by Django 4.2 on 2023-05-09 17:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('parts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assembly',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=50, unique=True, verbose_name='Designation')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Date of change')),
            ],
            options={
                'verbose_name': 'Assembly',
                'verbose_name_plural': 'Assemblies',
                'ordering': ('designation',),
            },
        ),
        migrations.CreateModel(
            name='AssemblyPart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_count', models.PositiveIntegerField(default=1, verbose_name='Quantity')),
                ('assembly', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assemblies.assembly', verbose_name='Assembly')),
                ('part', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='parts.part', verbose_name='Part')),
            ],
            options={
                'verbose_name': 'Part in assembly',
                'verbose_name_plural': 'Parts in assembly',
            },
        ),
        migrations.AddField(
            model_name='assembly',
            name='parts',
            field=models.ManyToManyField(blank=True, through='assemblies.AssemblyPart', to='parts.part', verbose_name='Parts'),
        ),
    ]
