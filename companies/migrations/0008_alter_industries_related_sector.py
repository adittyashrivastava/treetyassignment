# Generated by Django 3.2.17 on 2023-02-12 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0007_auto_20230211_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='industries',
            name='related_sector',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='companies.sectors'),
        ),
    ]
