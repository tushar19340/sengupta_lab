# Generated by Django 3.2.4 on 2021-06-10 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sengupta_lab', '0021_about'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paper',
            old_name='subText',
            new_name='journal_name',
        ),
        migrations.AlterField(
            model_name='paper',
            name='imageUrl',
            field=models.TextField(help_text='<p style="color:darkgreen">*<b>IMPORTANT: </b>Landscape Orientation Only (Width of image should be more than height)*</p>'),
        ),
        migrations.AlterField(
            model_name='team',
            name='imageUrl',
            field=models.TextField(help_text='<p style="color:darkgreen">*<b>IMPORTANT </b> Square Dimensions Only*</p>'),
        ),
    ]
