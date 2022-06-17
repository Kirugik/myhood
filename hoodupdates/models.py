from django.db import models
from django.contrib.auth.models import User 
from url_or_relative_url_field.fields import URLOrRelativeURLField 

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='profile')
    bio = models.TextField()
    id_number = models.TextField(max_length=100, null=True, blank=True) 
    profile_picture = models.ImageField(upload_to='profiles_pics/')
    full_name = models.CharField(max_length=120, blank=True)
    profession = models.CharField(max_length=120, blank=True) 
    contact = models.EmailField(null=True, blank=True)
    hood = models.ForeignKey('Hood', on_delete=models.SET_NULL, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)  

    website= URLOrRelativeURLField(null=True,blank=True)
    facebook =URLOrRelativeURLField(null=True,blank=True)
    instagram = URLOrRelativeURLField(null=True,blank=True)
    twitter = URLOrRelativeURLField(null=True,blank=True)

    def __str__(self):
        return str(self.user.username)




class Hood(models.Model):
    name = models.CharField(max_length=50)
    located = models.CharField(max_length=60)  
    occupants_count = models.IntegerField(null=True, blank=True) 
    description = models.TextField(max_length=200, blank=True)  
    hood_image = models.ImageField(upload_to='hood_images/')
    police_contact = models.CharField(max_length=50, null=True, blank=True)
    health_dept_contact = models.CharField(max_length=50, null=True, blank=True)
    hood_admin = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    since = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name) 


    def create_hood(self):
        self.save()

    def update_hood(self):
        self.save()

    def delete_hood(self):
        self.delete()

    @classmethod
    def find_hood(cls, hood_id):
        return cls.objects.filter(id=hood_id)



class Business(models.Model):
    business_name = models.CharField(max_length=100)
    business_description = models.TextField(max_length=255, blank=True) 
    business_logo = models.ImageField(upload_to='business_logos/')
    business_owner = models.ForeignKey(Profile,on_delete=models.CASCADE, related_name='business')
    location = models.ForeignKey(Hood, on_delete=models.CASCADE, related_name='business')
    date_started = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return str(self.business_name)

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()
        
    def find_business(self,business_id):
        business = Business.objects.filter(self = business_id)
        return business

    # @classmethod
    # def search_business(cls, name):
    #     return cls.objects.filter(name__icontains=name).all()



class Update(models.Model):
    title = models.CharField(max_length=100, null=True)
    details = models.TextField(null=True) 
    posted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='post_owner')
    hood = models.ForeignKey(Hood, on_delete=models.CASCADE, related_name='hood_post')

    def __str__(self):
        return str(self.title) 

    def new_update(self):
        self.save()

    def delete_update(self):
        self.delete()
