from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.

class User(AbstractUser):
    '''
    This class represents the user table
    It automatically inherits the following fields from AbstractUser:
        username, first_name, last_name, email, password, groups, user_permissions, is_staff, is_active, is_superuser, last_login, date_joined, is_admin and id
    Dependencies: None
        * if I delete a user, it will delete all of their beverages
    Relationship: One to Many (User to Beverage)

    '''
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    related_name ='users'

    # ! adding to repair ERROR: Reverse accessor 'Group.user_set' for 'auth.User.groups' clashes with reverse accessor for 'sulphite_safe_api.User.groups'
    groups = models.ManyToManyField(Group, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions')

    def __str__(self):
        return self.username
    # this is a magic method that returns the username of the user when the user object is printed

class Beverage(models.Model):
    '''
    This class represents the beverage table
    Dependencies: User, BeverageSulphiteStatus, UserBeverageSulphiteStatus
        * if I delete a user, it will delete all of their beverages
        * if I delete a beverage, it will delete all of its beverage sulphite statuses and user beverage sulphite statuses
    Relationship: One to Many (User to Beverage)
    '''
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='beverages', default=1)

    def __str__(self):
        return self.name

class SulphiteStatus(models.Model):
    '''
    This class represents the sulphite status table
    Dependencies: User, BeverageSulphiteStatus, UserBeverageSulphiteStatus
        * if I delete a user, it will delete all of their sulphite statuses
        * if I delete a sulphite status, it will delete all of its beverage sulphite statuses and user beverage sulphite statuses
    Relationship: Many to Many (Beverage to SulphiteStatus)
    '''
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sulphite_statuses', default=1)
    beverages = models.ManyToManyField(Beverage, through='BeverageSulphiteStatus')
        # through: 'BeverageSulphiteStatus' is used to specify the intermediate table
        # this will create a Many to Many relationship between Beverage and SulphiteStatus without creating a new table and will allow us to add additional fields to the intermediate table. It prevents the creation of a new table called 'beverage_sulphite_status' and instead uses the BeverageSulphiteStatus table. This is better because it allows us to add additional fields to the intermediate table and it also allows us to use the intermediate table as a model in our views.py file. If we were to use the ManyToManyField without the through parameter, we would not be able to use the intermediate table as a model in our views.py file.

    def __str__(self):
        return self.name

class BeverageSulphiteStatus(models.Model):
    '''
    This class represents the beverage sulphite status table
    Dependencies: User, Beverage, SulphiteStatus, UserBeverageSulphiteStatus
        * if I delete a user, it will delete all of their beverage sulphite statuses
        * if I delete a beverage, it will delete all of its beverage sulphite statuses and user beverage sulphite statuses
        * if I delete a sulphite status, it will delete all of its beverage sulphite statuses and user beverage sulphite statuses
        * if I delete a beverage sulphite status, it will delete all of its user beverage sulphite statuses
    Relationship: Many to Many (Beverage to SulphiteStatus)
    '''
    beverage = models.ForeignKey(Beverage, on_delete=models.CASCADE, related_name='beverage_sulphite_statuses')
    sulphite_status = models.ForeignKey(SulphiteStatus, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='beverage_sulphite_statuses', default=1)

    def __str__(self):
        return self.beverage.name + ' ' + self.sulphite_status.name

class UserBeverageSulphiteStatus(models.Model):
    '''
    This class represents the user beverage sulphite status table
    Dependencies: User, BeverageSulphiteStatus, Beverage, SulphiteStatus
        * if I delete a user, it will delete all of their user beverage sulphite statuses
        * if I delete a beverage, it will delete all of its user beverage sulphite statuses
        * if I delete a sulphite status, it will delete all of its user beverage sulphite statuses
        * if I delete a beverage sulphite status, it will delete all of its user beverage sulphite statuses
    Relationship: Many to Many (User to BeverageSulphiteStatus)
    User will automatically be allocated a beverage sulphite status when they create a new beverage
    '''
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=1)
    beverage_sulphite_status = models.ForeignKey(BeverageSulphiteStatus, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user) + ' ' + str(self.beverage_sulphite_status)
