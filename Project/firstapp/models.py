from django.db import models
from font_icons.models import IconForeignKeyField


# ---------------------------------------      Technology     ---------------------------------- 
class Technology(models.Model):
    # technology settles in this stock
    icon = IconForeignKeyField(blank=True,null=True)
    title = models.CharField(blank=True,null=True,max_length=127)
    short_description = models.CharField(blank=True,null=True,max_length=127)


    def __str__(self):
        return self.title



# ---------------------------------------      About     ---------------------------------- 

class About(models.Model):
    title = models.CharField(blank=True,null=True,max_length=150)
    text =models.TextField(blank=True,null=True)
    image = models.ImageField('Sekil', upload_to='about_image')



    def __str__(self):
        return self.title



# ---------------------------------------      Choose     ---------------------------------- 

class Choose(models.Model):
    icon = IconForeignKeyField(blank=True,null=True)
    title = models.CharField(blank=True,null=True,max_length=150)
    short_description = models.CharField(blank=True,null=True,max_length=127)
    video = models.FileField('Video' , upload_to='Choose_uploaded',null=True,blank=True)


    def __str__(self):
        return self.title



# ---------------------------------------      Team     ---------------------------------- 

class Team(models.Model):
    name = models.CharField(blank=True,null=True,max_length=150)
    mission =models.CharField(blank=True,null=True,max_length=150)
    image = models.ImageField('Sekil', upload_to='team_image')

    def __str__(self):
        return self.name



# ---------------------------------------      Case     ---------------------------------- 
class Case(models.Model):
    title = models.CharField(blank=True,null=True,max_length=150)
    short_info =models.CharField(blank=True,null=True,max_length=150)
    image = models.ImageField('Sekil', upload_to='Case_image')
    short_description = models.CharField(blank=True,null=True,max_length=127)
    icon = IconForeignKeyField(blank=True,null=True)


    def __str__(self):
        return self.title



# ---------------------------------------      Work     ---------------------------------- 
class Work(models.Model):
    title = models.CharField(blank=True,null=True,max_length=150)
    short_description = models.CharField(blank=True,null=True,max_length=127)
    icon = IconForeignKeyField(blank=True,null=True)


    def __str__(self):
        return self.title



# ---------------------------------------      Blog     ---------------------------------- 
class Blog(models.Model):
    title = models.CharField(blank=True,null=True,max_length=150)
    image = models.ImageField('Sekil', upload_to='Blog_image')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    # icon = IconForeignKeyField(blank=True,null=True)
    # date = models.DateField()


    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(blank=True,null=True,max_length=150)
    icon = IconForeignKeyField(blank=True,null=True)

    def __str__(self):
        return self.name


# ---------------------------------------      News     ---------------------------------- 
class News(models.Model):
    title = models.CharField(blank=True,null=True,max_length=150)
    image = models.ImageField('Sekil', upload_to='News_image')
    # icon = IconForeignKeyField(blank=True,null=True)
    # date = models.DateField()


    def __str__(self):
        return self.title


    class Meta:
        verbose_name_plural = "news"








# ---------------------------------------      Contact     ---------------------------------- 
class Contact(models.Model):
    full_name = models.CharField(blank=True,null=True,max_length=150)
    email = models.EmailField(blank=True,null=True,max_length=150)
    subjec = models.CharField(blank=True,null=True,max_length=150)
    message = models.TextField(blank=True,null=True,help_text='Send your message', max_length=150)


    def __str__(self):
        return self.full_name

    # moderetion
    created_at = models.Datefield(auto_now_add=True)
    updated_at = models.Datefield(auto_now=True)


    class Meta:
        verbose_name_plural = "Contacts"
        ordering = ('-created_at')
