# Generated by Django 3.2.4 on 2021-06-07 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sengupta_lab', '0004_news_research_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
