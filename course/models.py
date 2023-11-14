from django.db import models
from django.contrib.auth import get_user_model
from .utils import generate_slug
# Create your models here.
User = get_user_model()


class Package(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to="images/package")
    description = models.TextField()
    bg_image = models.ImageField(upload_to="images/package")

    def __str__(self) -> str:
        return self.name

    def getItems(self):
        return self.items.split(",")

    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.name)
        super(Package, self).save(*args, **kwargs)


class Course(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    about = models.CharField(max_length=250)
    likes = models.IntegerField(default=0)
    image = models.ImageField(upload_to="images/course")

    def __str__(self) -> str:
        return self.name


class PackageTaken(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.package.name + " - " + self.user.get_username()


class Earning(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    earned = models.IntegerField(default=0)

    def __str__(self):
        return self.user.get_username()


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=200)
    is_success = models.BooleanField()
