from django.db.models.base import Model
from ckeditor.fields import RichTextField

from djongo import models

class Home(models.Model):

    image_desc = '<p style="color:red">*<b>IMPORTANT </b> All the Image should be of same ratio. Use landscape orientation*</p>'

    # bold_help = "To make text bold, wrap it inside this tag: &lt;b&gt; Your text &lt;/b&gt;"
    # italic_help = "To make italicize your text, wrap your text inside &lt;i&gt; Your text &lt;/i&gt;"
    # color_help = 'To add color to a text, wrap your text inside &lt;span style="color:#4287f5" &gt; Your text &lt;/span&gt;'

    # text_desc = '<p style="color:green">*<b>IMPORTANT </b> <br>' + bold_help +  '<br>' + italic_help + '<br>' + color_help + '<br> So basically you can write HTML in it *</p>'
    image_url1 = models.TextField()
    image_url2 = models.TextField(blank=True, null=True, help_text=image_desc)
    image_url3 = models.TextField(blank=True, null=True, help_text=image_desc)
    image_url4 = models.TextField(blank=True, null=True, help_text=image_desc)
    image_url5 = models.TextField(blank=True, null=True, help_text=image_desc)
    text_para = RichTextField()

    class Meta:
        verbose_name_plural = "Home"

class Footer(models.Model):

    address = RichTextField(blank=True, null=True)
    contact_email = models.CharField(max_length=100)
    contact_phone = models.CharField(max_length=50)
    purpose = models.TextField()

    image_1 = models.TextField(blank=True, null=True)
    image_2 = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Footer"


class Papers_Category(models.Model):
    name = models.CharField("Add new category", max_length=20)
    # color = models.CharField("Add color of the tag", max_length=10)
    class Meta:
        verbose_name_plural = "Papers Category"

    def __str__(self):
        return self.name

class Paper(models.Model):
    # choices = (
    #     ("ml", "Machine Learning"),
    #     ("genomics", "Genomics"),
    #     ("other", "Other"),
    # )

    title = models.CharField("Paper Title", max_length=100)
    imageUrl = models.TextField(help_text='<p style="color:darkgreen">*<b>IMPORTANT: </b>Landscape Orientation Only (Width of image should be more than height)*</p>')
    date = models.DateField(blank=True, null=True)
    authors = models.CharField(max_length=200)
    journal_name = models.CharField(max_length=100)
    doiLink = models.TextField()
    abstract = RichTextField()

    category = models.ManyToManyField(Papers_Category, blank=True)

    class meta:
        verbose_name_plural = 'Publications'

    def __str__(self):
        return self.title



class Team(models.Model):
    choices = (
        ("Btech", "Btech "),
        ("Mtech", "Mtech"),
        ("PHD", "PHD"),
        ("Other", "other")
    )

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=25,choices=choices, default='other')
    imageUrl = models.TextField(help_text='<p style="color:darkgreen">*<b>IMPORTANT </b> Square Dimensions Only*</p>')
    designation = models.CharField(max_length=100)
    about = RichTextField()
    email = models.CharField(max_length=100)
    github = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Team"

    def __str__(self):
        return self.name



class News(models.Model):

    title = models.CharField(max_length=100)
    image_url = models.TextField(blank = True, null = True)
    date = models.DateField()
    sub_text = models.TextField(blank = True, null = True)
    link = models.TextField()
    desc = models.TextField(blank = True, null = True)

    class Meta:
        verbose_name_plural = "News"

    def __str__(self):
        return self.title


class Research(models.Model):
    
    title = models.TextField()
    image_Url = models.TextField()
    info = RichTextField()
    publication_details = RichTextField()

    class meta:
        verbose_name_plural = 'Research'

    def __str__(self):
        return self.title


class Software_Tag(models.Model):
    name = models.CharField("Tag Name", max_length=20)
    color = models.CharField("Add color of the tag", max_length=10)

    class Meta:
        verbose_name_plural = "Software Tags"

    def __str__(self):
        return self.name

class Software(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    github_link = models.CharField(max_length=250)

    tags = models.ManyToManyField(Software_Tag, blank = True)
    
    def __str__(self):
        return self.title

class About(models.Model):
    img_url = models.TextField()
    About = RichTextField()

    class Meta:
        verbose_name_plural = "About"

    
