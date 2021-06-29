from django.db import models
import re



EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'\d.*[A-Z]|[A-Z].*\d')

class UserManager(models.Manager):
    def validator(self, post_data):
        errors = {}

        
        if(len(post_data['first_name'])) < 2:
            errors['first_name'] = "First name must at least 2 characters"
        
        if(len(post_data['last_name'])) < 2:
            errors['last_name'] = "Last name must be at least 2 characters"

        if len(post_data['email']) < 1:
            errors['email'] = "email must be more than 1 character"
        elif not EMAIL_REGEX.match(post_data['email']):
            errors['email'] = "email must be a valid email address"

        try:
            User.objects.get (email= post_data ['email'])
            errors ['email']= 'Email is already in use.'
        except:
            pass
        
        
        if len(post_data['password']) < 8:
            errors['password'] = "Password must be at least 8 characters"
        
        if post_data['password'] != post_data ['confirm_password']:
            errors['password_match'] = "Passwords do not match!!!"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()