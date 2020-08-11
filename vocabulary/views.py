from django.shortcuts import render,HttpResponseRedirect,get_object_or_404,redirect
from django.urls import reverse, reverse_lazy

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from . forms import CommentCreation

from django.views.generic import CreateView, UpdateView, ListView, DetailView, View, TemplateView, DeleteView
from . models import Vocabulary, Comment, MyList

class WordList(ListView):
    context_object_name='words'
    model=Vocabulary
    template_name='vocabulary/wordlist.html'

@login_required
def AddToMyList(request,pk):
    word=get_object_or_404(Vocabulary,pk=pk)
    print(word)
    wordtolist=MyList.objects.get_or_create(vocab=word, user=request.user)
    wordtolist[0].save()
    return HttpResponseRedirect(reverse('vocabulary:wordlist'))
    
#Try this using ClassbasedView
@login_required
def MyListView(request):

    words=MyList.objects.filter(user=request.user)
  
    #worduser=request.user.mylist.all()/it also works
    
    print(words)
    
    return render(request,'vocabulary/mylist.html',context={'words':words})
@login_required
def WordDetail(request,pk):
    word=Vocabulary.objects.get(pk=pk)
    """   comments=Comment.objects.filter(word=word)
    print(comments) """
    form=CommentCreation()
    context={'word':word,'form':form}
    if request.method=='POST':
        form=CommentCreation(request.POST)
        if form.is_valid:
            instance=form.save(commit=False)
            instance.user=request.user
            instance.word=word
            instance.save()
            return HttpResponseRedirect(reverse('vocabulary:worddetail', kwargs={'pk':pk}))
    return render(request,'vocabulary/worddetail.html',context)

