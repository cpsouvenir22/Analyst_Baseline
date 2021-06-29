from django.contrib.messages.api import error
from django.shortcuts import render, HttpResponse, redirect
from .models import Event,Group
from django.apps import apps
User = apps.get_model('login_app','User')
from django.contrib import messages

# Create your views here.
def intel_index (request):
    context = {
        "Groups": Group.objects.all(),
        "Events": Event.objects.all()
    }
    
    return render (request, "intelpage.htm", context)

def create_group (request):
    errors = Group.objects.basic_validator (request.POST)

    if errors:
        for k, v in errors.items():
            messages.error(request, v)
            print (errors)
        return redirect('/intel')
        
    Group.objects.create(
            group_name = request.POST['group_name'],
            description= request.POST['description'],
            creator = User.objects.get(id= request.session['user_id'])

        )

    print("group added")

    return redirect ('/intel')

def create_event (request):

    errors = Event.objects.basic_validator (request.POST)

    if errors:
        for k, v in errors.items():
            messages.error(request, v)
            print (errors)
        return redirect('/intel')
        
    Event.objects.create(
            event_name = request.POST['event_name'],
            event_date = request.POST['event_date'],
            group = Group.objects.get(id= request.POST['group']),
            creator = User.objects.get(id= request.session['user_id']),
            description = request.POST['description']
        )


    return redirect ('/intel')

def group_page (request, group_id):
    context = {
        'group': Group.objects.get (id= group_id),
        
    }
    return render (request, "groups.htm", context)

def event_page (request, event_id):
    context = {
        'event': Event.objects.get (id= event_id)
    }
    return render (request, "EventPage.htm", context)

def destroy_group (request, group_id):
    group = Group.objects.get(id= group_id)
        
    group.delete ()
    return redirect ('/intel')

def destroy_event (request, event_id):
    event = Event.objects.get(id= event_id)
    if event.creator.id != request.session['user_id']:
        messages.info(request, f"Event can only be deleted by creator")
        return redirect ('/intel')
    event.delete ()

    return redirect ('/intel')



