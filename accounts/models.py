from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _
from django_countries.fields import CountryField
from django.urls import reverse
import datetime
from django.db.models.signals import post_save
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,verbose_name=_('User'),on_delete=models.CASCADE)
    address=models.CharField(max_length=100)
    country=CountryField()
    image=models.ImageField(upload_to='profile_img/',blank=True,null=True,verbose_name=_('Image'))
    slug=models.SlugField(blank=True,null=True)
    joindata=models.DateTimeField(verbose_name=_("Join Date"),default=datetime.datetime.now)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)


    class Meta():
        verbose_name=("Profile")
        verbose_name_plural=("Profiles")

    def __str__(self):
        return '%s'%self.user

    def get_absolute_url(self):
        return reverse('accounts:product_detail',kwargs={'slug':self.slug})


def create_profile(sender,**kwargs):
    if kwargs['created']:
        user_profile=Profile.objects.create(user=kwargs['instance'])



post_save.connect(create_profile,sender=User)