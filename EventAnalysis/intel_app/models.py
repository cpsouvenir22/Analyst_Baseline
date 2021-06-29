from django.db import models
from django.db.models.fields import related
from login_app.models import User

class GroupManager(models.Manager):
    def basic_validator(self, post_data):

        errors = {}
        if len (post_data['group_name']) < 3:
            errors['group_name'] = "You must enter a group name"

        if len (post_data['description']) < 3:
            errors['group'] = "Please enter a brief synopsis of the group"

        return errors

    
class Group (models.Model):
    group_name = models.CharField("Group Name",max_length=20)
    description = models.TextField("Description")
    creator = models.ForeignKey (User, related_name = "groups", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = GroupManager ()

class EventManager(models.Manager):
    def basic_validator(self, post_data):

        errors = {}
        if len (post_data['event_name']) < 5:
            errors['event_name'] = "You must enter an event name"

        if len (post_data['description']) < 10:
            errors['description'] = "Please provide event details"
        
        return errors

class Event (models.Model):
    event_name = models.CharField("Event Name",max_length=20)
    event_date = models.DateField("Date of Event")
    group = models.ForeignKey(Group, related_name= "activities", on_delete=models.CASCADE)
    creator = models.ForeignKey (User, related_name = "events", on_delete=models.CASCADE)
    description = models.TextField("Description of Event")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = EventManager ()




