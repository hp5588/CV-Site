from django.db import models


# Create your models here.
class Experience(models.Model):
    title = models.CharField(max_length=100)
    department = models.CharField(max_length=100, blank=True)
    position = models.CharField(max_length=50)
    description = models.TextField()
    start_date = models.DateField('start date')
    end_date = models.DateField('end date')


class Education(models.Model):
    university = models.CharField(max_length=100)
    country = models.CharField(max_length=20, default="")
    major = models.CharField(max_length=100)
    start_date = models.DateField('start date')
    end_date = models.DateField('end date')
    description = models.TextField(default="")


class Skill(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey('SkillCategory', on_delete=models.DO_NOTHING, null=True)
    level = models.IntegerField('level of skill range from 0 to 10', blank=True, null=True)

    def get_category(self):
        return self.category
        # return self.category.name

    def __str__(self):
        return self.name


class SkillCategory(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=9)
    collapse = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Framework(models.Model):
    name = models.CharField(max_length=100)
    skill = models.ForeignKey('Skill', on_delete=models.DO_NOTHING, null=True)
    show_skill = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.name

    def full_name(self):
        if self.show_skill:
            return "%s - %s" % (self.name, self.skill.name)
        return self.name


class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="portfolio/images")
    description = models.TextField()
    rank = models.IntegerField()
    link = models.TextField(default="")

    def __str__(self):
        return self.name


class Tag(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    framework = models.ForeignKey(Framework, on_delete=models.CASCADE)

    def __str__(self):
        return self.portfolio.name

