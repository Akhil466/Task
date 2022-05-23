from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from . models import Task
from. forms import todoform
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView,DeleteView

# Create your views here.
class tasklistview(ListView):
    model=Task
    template_name = 'home1.html'
    context_object_name = 'task1'

class taskdetailview(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'

class taskupdateview(UpdateView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')
    fields=('name','priority','date')

class taskdeleteview(DeleteView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'

    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})


def demo(request):
    task1=Task.objects.all()

    if request.method=='POST':
        name=request.POST.get('name','')
        priority = request.POST.get('priority', '')
        date= request.POST.get('date','')
        task=Task(name=name,priority=priority,date=date)
        task.save()

    return render(request,'home1.html',{'task1':task1})
# def detail(request):
#
#     return render(request,'detail.html',{'task':task})
def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')

    return render(request,'delete.html')
def update(request,id):
    task=Task.objects.get(id=id)
    form=todoform(request.POST or None,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'task':task,'form':form})