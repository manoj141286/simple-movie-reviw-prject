from django.shortcuts import render
from testapp.models import movie
from testapp.forms import movieForm
# Create your views here.
def index_view(request):
    return render(request,'testapp/index.html')

def Addmovie_View(request):
    form=movieForm()
    my_dict={'form':form}
    if request.method=="POST":
        form=movieForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index_view(request)
    return render(request,'testapp/addmovie.html',context=my_dict)

def listmovie_view(request):
    movies_list=movie.objects.all()
    my_dict={"movies_list":movies_list}
    return render(request,"testapp/listmovie.html",context=my_dict)
