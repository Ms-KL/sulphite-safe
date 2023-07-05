
'''
This test file is used to test the models.py file.
To run the tests, run the following command in the terminal from the root directory, which is:
sulphite_safe_project:
python manage.py test sulphite_safe_api.tests
'''

from django.test import TestCase

from .models import User, Beverage, SulphiteStatus, BeverageSulphiteStatus, UserBeverageSulphiteStatus

class UserTestCase(TestCase):
    def setUp(self):
        # create a user
        User.objects.create(
            username="test_user",
            password="test_password",
            email=""
        )

    def test_user_exists(self):
        # get the user
        user = User.objects.get(username="test_user")
        # check that the user exists
        self.assertTrue(user)

class BeverageTestCase(TestCase):
    def setUp(self):
        # create a user
        user = User.objects.create(
            username="test_user",
            password="test_password",
            email=""
        )
        # create a beverage
        Beverage.objects.create(
            name="test_beverage", 
            description="test_description",
            user=user,
        )

    def test_beverage_exists(self):
        # get the beverage
        beverage = Beverage.objects.get(name="test_beverage")
        # check that the beverage exists
        self.assertTrue(beverage)

class SulphiteStatusTestCase(TestCase):
    def setUp(self):
        # create a user
        user = User.objects.create(
            username="test_user",
            password="test_password",
            email=""
        )

        # create a sulphite status
        SulphiteStatus.objects.create(
            name="test_sulphite_status",  
            description="test_description",
            user=user,
        )

    def test_sulphite_status_exists(self):
        # get the sulphite status
        sulphite_status = SulphiteStatus.objects.get(name="test_sulphite_status")
        # check that the sulphite status exists
        self.assertTrue(sulphite_status)

class BeverageSulphiteStatusTestCase(TestCase):
    def setUp(self):
        # create a user
        user = User.objects.create(
            username="test_user",
            password="test_password",
            email=""
        )
        # create a beverage
        beverage = Beverage.objects.create(
            name="test_beverage", 
            description="test_description",
            user=user,
        )
        # create a sulphite status
        sulphite_status = SulphiteStatus.objects.create(
            name="test_sulphite_status",  
            description="test_description",
            user=user,
        )
        # create a beverage sulphite status
        BeverageSulphiteStatus.objects.create(
            beverage=beverage,    
            sulphite_status=sulphite_status,
            user=user,
        )

    def test_beverage_sulphite_status_exists(self):
        # get the beverage sulphite status
        beverage_sulphite_status = BeverageSulphiteStatus.objects.get(beverage__name="test_beverage")
        # check that the beverage sulphite status exists
        self.assertTrue(beverage_sulphite_status)
    
    def test_delete_beverage(self):
        # get the beverage
        beverage = Beverage.objects.get(name="test_beverage")
        # delete the beverage
        beverage.delete()
        # check that the beverage does not exist
        self.assertFalse(Beverage.objects.filter(name="test_beverage").exists())

    def test_delete_sulphite_status(self):
        # get the sulphite status
        sulphite_status = SulphiteStatus.objects.get(name="test_sulphite_status")
        # delete the sulphite status
        sulphite_status.delete()
        # check that the sulphite status does not exist
        self.assertFalse(SulphiteStatus.objects.filter(name="test_sulphite_status").exists())

class UserBeverageSulphiteStatusTestCase(TestCase):
    def setUp(self):
        # create a user
        user = User.objects.create(
            username="test_user", 
            email="test_email",
            password="test_password",
        )
        # create a beverage
        beverage = Beverage.objects.create(
            name="test_beverage", 
            description="test_description",
            user=user,
        )
        # create a sulphite status
        sulphite_status = SulphiteStatus.objects.create(
            name="test_sulphite_status",  
            description="test_description",
            user=user,
        )
        # create a beverage sulphite status
        beverage_sulphite_status = BeverageSulphiteStatus.objects.create(
            beverage=beverage,    
            sulphite_status=sulphite_status,
            user=user,
        )
        # create a user beverage sulphite status
        UserBeverageSulphiteStatus.objects.create(
            user=user,    
            beverage_sulphite_status=beverage_sulphite_status,
        )

    def test_user_beverage_sulphite_status_exists(self):
        # get the user beverage sulphite status
        user_beverage_sulphite_status = UserBeverageSulphiteStatus.objects.get(user__username="test_user")
        # check that the user beverage sulphite status exists
        self.assertTrue(user_beverage_sulphite_status)

# I want to add tests for deleting an individual beverage and individual sulphite status while there is a beverage sulphite status that references them. Here is the code to be inserted. 

# do I need to add the below into one of teh above test classes?
# the answer is no, because the below tests are for deleting a beverage and a sulphite status, not for deleting a beverage sulphite status




