from django.test import TestCase
from .models import Profile, Hood, Business, Update

# Create your tests here.
class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.user = Profile(user='Robert')
        self.user.save()
        self.new_profile = Profile(user = self.user, bio='This is my bio', id_number='123456789', profile_picture='profilepicture.jpeg', full_name='Robert Kirui', profession='software developer', contact='robert.kirui@student.moringaschool.com', hood='Nairobi') 

    # TearDown Method
    def tearDown(self):
        Profile.objects.all().delete()
    
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile, Profile))
    
    # Testing Save Method
    def test_save_profile(self):
        self.new_profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0) 
    
    # Testing Delete Method
    def test_delete_profile(self):
        self.new_profile.save_profile()
        self.new_profile.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)



class HoodTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.user = Profile(user='Robert')
        self.user.save()
        self.new_profile = Profile(user = self.user, bio='This is my bio', id_number='123456789', profile_picture='profilepicture.jpeg', full_name='Robert Kirui', profession='software developer', contact='robert.kirui@student.moringaschool.com', hood='Nairobi')
        self.new_hood = Hood(name='Nairobi', located='Nairobi City', occupants_count='2000000', description='It is a good city', hood_image='nairobi.jpeg', police_contact='111', health_dept_contact='222', hood_admin=self.new_profile)
        
    # TearDown Method
    def tearDown(self):
        Profile.objects.all().delete()
        Hood.objects.all().delete()
        
    
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_hood, Hood))
        
    # Testing Save Method
    def test_save_hood(self):
        self.new_hood.save_hood()
        hoods = Hood.objects.all()
        self.assertTrue(len(hoods) > 0)
        
    # Testing Delete Method
    def test_delete_hood(self):
        self.new_hood.save_hood()
        self.new_hood.delete_hood()
        hoods = Hood.objects.all()
        self.assertTrue(len(hoods) == 0) 



class BusinessTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.new_profile = Profile(user = self.user, bio='This is my bio', id_number='123456789', profile_picture='profilepicture.jpeg', full_name='Robert Kirui', profession='software developer', contact='robert.kirui@student.moringaschool.com', hood='Nairobi')
        self.new_profile.save()

        self.new_hood = Hood(name='Nairobi', located='Nairobi City', occupants_count='2000000', description='It is a good city', hood_image='nairobi.jpeg', police_contact='111', health_dept_contact='222', hood_admin=self.new_profile)
        self.new_hood.save() 

        self.new_business = Business(business_name='Example Business', business_description='This is my new business', business_logo='businesslogo.jpeg', business_owner='Robert', hood=self.new_hood) 
        
    # TearDown Method
    def tearDown(self):
        Profile.objects.all().delete()
        Hood.objects.all().delete()
        Business.objects.all().delete()
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_business, Business))

    # Testing Save Method      
    def test_save_business(self):
        self.new_business.save_business()
        businesses = Business.objects.all()
        self.assertTrue(len(businesses) > 0)

    # Testing Delete Method 
    def test_delete_business(self):
        self.new_business.save_business()
        self.new_business.delete_business()
        businesses = Business.objects.all()
        self.assertTrue(len(businesses) == 0)



class UpdateTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.new_profile = Profile(user = self.user, bio='This is my bio', id_number='123456789', profile_picture='profilepicture.jpeg', full_name='Robert Kirui', profession='software developer', contact='robert.kirui@student.moringaschool.com', hood='Nairobi')
        self.new_profile.save()

        self.new_hood = Hood(name='Nairobi', located='Nairobi City', occupants_count='2000000', description='It is a good city', hood_image='nairobi.jpeg', police_contact='111', health_dept_contact='222', hood_admin=self.new_profile)
        self.new_hood.save() 

        self.new_update = Update(title='Example update', details='This is an example update', user=self.new_profile, hood=self.new_hood)
    
    # TearDown Method
    def tearDown(self):
        Profile.objects.all().delete()
        Hood.objects.all().delete()
        Business.objects.all().delete()
        Update.objects.all().delete() 
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_update, Update)) 

    # Testing Save Method     
    def test_save_update(self):
        self.new_update.save_update()
        updates = Update.objects.all()
        self.assertTrue(len(updates) > 0)

    # Testing Delete Method   
    def test_delete_update(self):
        self.new_update.save_update()
        self.new_update.delete_update()
        updates = Update.objects.all()
        self.assertTrue(len(updates) == 0) 
