from django.shortcuts import render , redirect , get_object_or_404
from .forms import GarbageModel,GarbageForm

# Create your views here.

# index does two things at once so it has alot of code in comparison to normal
def index(request):
    garbage = GarbageModel.objects.all()  #this gathers all items for sale for display
    form = GarbageForm(request.POST or None)  #this gathers the form information and if it populated it will collect that data

    if request.method == 'POST' and form.is_valid():  # if the form was filled out correctly and the page loaded it
        form.save()  # this saved the forms data as long as above if statements are met
        context= \
            {
                'form':form, # populates the page with the form
                'garbageList':garbage  # populates the page with all garbage added
            }
        return render(request, 'BootCRUDApp/index.html',context)  #returns to the page with garbage added
    context = \
        {
            'form':form, # populates the page with an empty form
            'garbageList':garbage  # populates the page with all garbage
        }
    return render(request, 'BootCRUDApp/index.html',context)  # runs the page with the information for a form and all garbage

# in case someone entered the wrong information
def EditGarbage(request,garbageID):  #it gathers the ID number from the garbage during population of the index page to be sent
    garbage= get_object_or_404(GarbageModel, pk = garbageID)  # grabs the garbage based on the idnumber sent through
    form =GarbageForm(request.POST or None, instance=garbage)  # fills the form to be edited with the information from garbage that was gathered above
    if request.method == 'POST' and form.is_valid():  # makes sure the form is correctly filled out after reloading
        form.save()  # saves the form information to be updated
        return redirect('index') # returns to the index page

    context= \
        {
            'form':form  # adds the form with garbage filling it out
        }
    return render(request,'BootCRUDApp/EditGarbage.html',context)  # renders the page with the necessary information to be edited