# Generated by Django 3.2.4 on 2021-06-10 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sengupta_lab', '0026_delete_home'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url1', models.TextField()),
                ('image_url2', models.TextField()),
                ('image_url3', models.TextField()),
                ('text_para', models.TextField()),
            ],
        ),
    ]
