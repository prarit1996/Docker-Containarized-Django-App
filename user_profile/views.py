from django.shortcuts import render
from .models import UserProfile
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from django.urls import reverse
 

# Create your views here.
@csrf_protect
def profile_data(request):
  data = UserProfile.objects.all()[0]
  profile_details = {
    'name':data.name,
    'email': data.email,
    'profile_desc': data.profile_desc,
    'profile_tags': data.profile_tags
  }
  return render(request,'index.html',profile_details)

@csrf_protect 
def edit_profile_data(request, **kwargsgs):
  data = UserProfile.objects.all()[0]
  profile_details = {
      'name':data.name,
      'email': data.email,
      'profile_desc': data.profile_desc,
      'profile_tags': data.profile_tags
    }
  if request.method == "POST":
    print(request.POST['name'],request.POST['profile_desc'], request.POST['profile_tags'])
    name=profile_details['name'] if not request.POST['name'] else request.POST['name']
    profile_desc = profile_details['profile_desc'] if not request.POST['profile_desc'] else request.POST['profile_desc']
    profile_tags = profile_details['profile_tags'] if not request.POST['profile_tags'] else request.POST['profile_tags']
    UserProfile.objects.update(name=name, profile_desc=profile_desc,profile_tags=profile_tags)
    return HttpResponseRedirect(reverse("profile"))
  return render(request, 'profile.html',profile_details)