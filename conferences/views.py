from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Conference
from .models import Conference, ScheduleManager
from conferences.models import ScheduleForm


def conf_list(request):
  mymembers = Conference.objects.all().values()
  template = loader.get_template('list_of_conf.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

  
def details(request, id):
  mymember = Conference.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))
def details(request, id):
  mymember = Conference.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def conf_add(request):
  if request.method =="POST":
    Name = request.POST['conf']
    Category= request.POST['category']
    Date = request.POST['date']
    Venue= request.POST['venue']
    Theme= request.POST['theme']
    
    new_conf = Conference(Name=Name,Category=Category,Date=Date,Venue=Venue,Theme=Theme)
    new_conf.save()
    return HttpResponse('Conference has added')
  else:
    return render(request,'add.html')

def schedule_add(request):
    if request.method == "POST":
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('schedule_detail')
    else:
        form = ScheduleForm()
    return render(request, 'add_schedule.html', {'form': form})

def schedule_detail(request):
    schedules = ScheduleManager.objects.all()
    return render(request, 'schedule_detail.html', {'schedules': schedules})