from django.shortcuts import render
from .models import Cours
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
# Create your views here.
def listCours(request):
    
   courList= Cours.objects.all()
   print('test')
   return render(request,"cours/list.html",{"cours":courList})


class DisplayCours(ListView):
    model = Cours
    template_name="index.html"
    context_object_name="cours"
    
    def get_queryset(self):
        #eventList= Event.objects.filter(state=True).order_by('-evt_date')
        courList= Cours.objects.all()

        return courList