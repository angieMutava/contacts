from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from user_contacts.models import Phone, Person
from user_contacts.new_contact_form import ContactForm

# from user_contacts.new_contact_form import ContactForm

def home(request):
    return render_to_response('index.html')

def all_contacts(request):
    contacts = Phone.objects.all()
    return render_to_response('all.html', {'contacts': contacts})

def test_add_contact_route(self):
    response = self.client_stub.get('/add/')
    self.assertEqual(response.status_code, 200)

def add(request):
    person_form = ContactForm()
    return render(request, 'add.html', {'person_form' : person_form}, context_instance = RequestContext(request))

def create(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('all/')
    return render(request, 'add.html', {'person_form' : form}, context_instance = RequestContext(request))
