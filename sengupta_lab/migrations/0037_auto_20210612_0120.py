# Generated by Django 3.2.4 on 2021-06-11 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sengupta_lab', '0036_remove_footer_image_1'),
    ]

    operations = [
        migrations.AddField(
            model_name='footer',
            name='image_1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='footer',
            name='image_2',
            field=models.TextField(blank=True, null=True),
        ),
    ]