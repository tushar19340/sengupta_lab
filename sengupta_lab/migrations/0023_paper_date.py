# Generated by Django 3.2.4 on 2021-06-10 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sengupta_lab', '0022_auto_20210610_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]