# Generated by Django 3.2.4 on 2021-06-11 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sengupta_lab', '0035_footer_image_1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='footer',
            name='image_1',
        ),
    ]
