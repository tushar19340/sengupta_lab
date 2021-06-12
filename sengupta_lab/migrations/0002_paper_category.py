# Generated by Django 3.2.4 on 2021-06-07 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sengupta_lab', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='category',
            field=models.CharField(choices=[('ml', 'Machine Learning'), ('genomics', 'Genomics'), ('other', 'Other')], default='other', max_length=10),
        ),
    ]
