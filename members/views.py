from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context,request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    mydata = Member.objects.all()
    all_values = Member.objects.all().values()
    first_names = Member.objects.values_list('firstname')
    filtered_name = Member.objects.filter(firstname='Makary').values()
    filter_with_or = Member.objects.filter(firstname='Makary').values()|Member.objects.filter(firstname= 'Fukushima').values()
    firstletter = Member.objects.filter(firstname__startswith = 'J').values()
    template = loader.get_template('template.html')
    context = {
        'mymembers': mydata,
        'all_values': all_values,
        'first_names': first_names,
        'filtered_name':filtered_name,
        'filter_with_or': filter_with_or,
        'firstletter': firstletter,
    }
    return HttpResponse(template.render(context, request))
