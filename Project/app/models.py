from django.db import models
from font_icons.models import IconForeignKeyField
# from django.contrib.auth import get_user_model
# User= get_user_model
# ---------------------------------------      Technology     ----------------------------------
class Technology(models.Model):
    # Technology settles in this stock
    icon = IconForeignKeyField(blank=True, null=True)
    title = models.CharField(blank=True, null=True, max_length=127)
    short_description = models.CharField(blank=True, null=True, max_length=127)

    def __str__(self):
        return self.title

    # moderetion
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)



    # class Meta:
    #     verbose_name = 'Technology'
    #     verbose_name_plural = 'Technologies'
    #     ordering = ('-created_at',)

# ---------------------------------------      About     ----------------------------------
    # About settles in this stock


class About(models.Model):
    title = models.CharField(blank=True, null=True, max_length=150)
    text = models.TextField(blank=True, null=True)
    image = models.ImageField('Sekil', upload_to='about_image')

    def __str__(self):
        return self.title

    # moderetion
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)



    # class Meta:
    #     verbose_name = 'About'
    #     verbose_name_plural = 'Abouts'
        # ordering = ('-created_at',)

# ---------------------------------------      Choose     ----------------------------------

# Choose settles in this stock


class Choose(models.Model):
    icon = IconForeignKeyField(blank=True, null=True)
    title = models.CharField(blank=True, null=True, max_length=150)
    short_description = models.CharField(blank=True, null=True, max_length=127)
    video = models.FileField(
        'Video', upload_to='Choose_uploaded', null=True, blank=True)

    def __str__(self):
        return self.title
    # moderetion
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

 

    # class Meta:
    #     verbose_name = 'Choose'
    #     verbose_name_plural = 'Chooses'
        # ordering = ('-created_at',)

# ---------------------------------------      Team     ----------------------------------
#
    # Team settles in this stock


class Team(models.Model):
    name = models.CharField(blank=True, null=True, max_length=150)
    mission = models.CharField(blank=True, null=True, max_length=150)
    image = models.ImageField('Sekil', upload_to='team_image')

    def __str__(self):
        return self.name

    # moderetion
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)



    # class Meta:
    #     verbose_name = 'Team'
    #     verbose_name_plural = 'Teamsqdwqwdqw'
        # ordering = ('-created_at',)

# ---------------------------------------      Case     ----------------------------------

    # Case settles in this stock


class Case(models.Model):
    title = models.CharField(blank=True, null=True, max_length=150)
    short_info = models.CharField(blank=True, null=True, max_length=150)
    image = models.ImageField('Sekil', upload_to='Case_image')
    short_description = models.CharField(blank=True, null=True, max_length=127)
    icon = IconForeignKeyField(blank=True, null=True)

    def __str__(self):
        return self.title
    # moderetion
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)



    # class Meta:
    #     verbose_name = 'Case'
    #     verbose_name_plural = 'Cases'
        # ordering = ('-created_at',)

# ---------------------------------------      Work     ----------------------------------

    # Work settles in this stock


class Work(models.Model):
    title = models.CharField(blank=True, null=True, max_length=150)
    short_description = models.CharField(blank=True, null=True, max_length=127)
    icon = IconForeignKeyField(blank=True, null=True)

    def __str__(self):
        return self.title
    # moderetion
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)



    # class Meta:
    #     verbose_name = 'Work'
    #     verbose_name_plural = 'Works'
        # ordering = ('-created_at',)

# ---------------------------------------      Blog     ----------------------------------

    # Blog settles in this stock


class Blog(models.Model):
    title = models.CharField(blank=True, null=True, max_length=150)
    image = models.ImageField('Sekil', upload_to='Blog_image')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    # icon = IconForeignKeyField(blank=True,null=True)
    # date = models.DateField()

    def __str__(self):
        return self.title
    # moderetion
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)




class Category(models.Model):
    # information
    name = models.CharField(blank=True, null=True, max_length=150)
    image = models.ImageField('Sekil', upload_to='Category_image')

    def __str__(self):
        return self.name
    # moderetion
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = "Categories"
        # ordering = ('name', '-created_at')

# ---------------------------------------      News     ----------------------------------

    # News settles in this stock


class News(models.Model):
    title = models.CharField(blank=True, null=True, max_length=150)
    image = models.ImageField('Sekil', upload_to='News_image')
    # icon = IconForeignKeyField(blank=True,null=True)
    # date = models.DateField()

    def __str__(self):
        return self.title

#   # moderetion
    created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    # published = models.BooleanField('Is published' , default=True)

   
    class Meta:
        verbose_name = 'news'
        verbose_name_plural = "news"
        ordering = ('-created_at',)


# ---------------------------------------      Contact     ----------------------------------

# Contact settles in this stock
class Contact(models.Model):
    full_name = models.CharField(blank=True, null=True, max_length=150)
    email = models.EmailField(blank=True, null=True, max_length=150)
    subjec = models.CharField(blank=True, null=True, max_length=150)
    message = models.TextField(
        blank=True, null=True, help_text='Send your message', max_length=150)

    def __str__(self):
        return self.full_name

    # moderetion
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    # published = models.BooleanField('Is published' , default=True)
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = "Contacts"
        # ordering = ('-created_at',)
