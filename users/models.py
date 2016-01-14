#-*- encoding=UTF-8 -*-
from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    #current_student = models.BooleanField(default=True)
    #activation_key = models.CharField(max_length=40, blank=True)
    # default active time is 15 minutes
    #active_time = models.DateTimeField(default=lambda: datetime.now() + timedelta(minutes=15))

    def __unicode__(self):
        return self.user.username


class Account(models.Model):
    username = models.CharField(max_length=20, default='', unique=True)
    nickname = models.CharField(max_length=20, default='', unique=True)

    TEACHER = 'TE'
    STUDENT = 'ST'
    OFFICER = 'OF'
    ALUMNUS = 'AL'
    IDENTITY_CHOICES = (
        (ALUMNUS, '校友'),
        (OFFICER, '職員'),
        (STUDENT, '學生'),
        (TEACHER, '教師')
    )

    ADMIN = 'ADMIN'
    JUDGE = 'JUDGE'
    USER = 'USER'
    USER_LEVEL_CHOICE = (
        (ADMIN, 'Admin'),
        (JUDGE, 'Judge'),
        (USER, 'User'),
    )

    identity = models.CharField(max_length=2, choices=IDENTITY_CHOICES, default=None)
    major = models.CharField(max_length=20, default='', blank=True, null=True)
    email = models.EmailField(max_length=250, unique=True)
    cellphone = models.CharField(max_length=10, unique=True, validators=[RegexValidator(regex='^\d{10}$', message='Invalid number', code='Invalid number')])
    ID_card = models.CharField(max_length=10, unique=True, validators=[RegexValidator(regex='^([A-Z][12]\d{8})$', message='Invalid id number', code='Invalid id number')])
    #score of photos description
    photos_rank = models.FloatField(default=0)
    user_level = models.CharField(max_length=9, choices=USER_LEVEL_CHOICE, default=USER)
    is_agree = models.BooleanField(default=False)



    def __unicode__(self):
        return self.username

    def updatePhotosRank(self):
        count = 0
        rank_sum = 0
        for photo in self.photos.all():
            rank_sum += photo.rank
            count += 1
        if count > 0:
            self.photos_rank = 1.0*rank_sum/count
        else:
            self.photos_rank = 0

        self.save(update_fields=['photos_rank'])

    '''custom authentication resolve 'is_authenticated' problem'''
    def is_authenticated(self):
        return True

    @property
    def is_superuser(self):
        return self.is_admin

    def is_active(self):
        return True

    def is_admin(self):
        return False

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    def has_judge_auth(self):
        has_auth = ((self.user_level == self.ADMIN) or (self.user_level == self.JUDGE))
        return has_auth
