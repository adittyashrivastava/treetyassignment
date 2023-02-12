# Generated by Django 3.2.17 on 2023-02-10 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_companies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companies',
            name='current_price',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='companies',
            name='ebitda',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='companies',
            name='full_time_employees',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='companies',
            name='long_business_summary',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='companies',
            name='marketcap',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='companies',
            name='revenue_growth',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='companies',
            name='weight',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='industries',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]
