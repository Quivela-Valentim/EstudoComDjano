from django.shortcuts import render
from .models import Topic, Entry
from .forms import Topicform, Entryform 
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    """Página Principal do estudo_Djanos"""
    return render(request, 'estudo_Djangos/index.html')

def topics(request):
    """Mostrando os tópicos na tela"""
    topics= Topic.objects.order_by('date')
    context = {'topics': topics}
    return render(request, 'estudo_Djangos/topics.html', context)
def topic(request, topic_id):
    """Página de anotações de tópicos """
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'estudo_Djangos/topic.html', context)

def new_topic(request):
    """Mostrando o formulário na tela dos tópicos """
    if request.method !='POST':
        # Não foi  submetido nehum dado, cria um formulário em branco 
        form = Topicform()
    
    else:
        # Dados submetidos pelo método POST, cria formulário
        form = Topicform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topics'))
    
    context ={'form': form}
    return render(request, 'estudo_Djangos/new_topic.html', context)

def new_entry(request, topic_id):
    """Mostrando o formulário das anotações """
    topic = Topic.objects.get(id=topic_id)
    
    if request.method != 'POST':
        #Nenhum dado fornecido, cria uma formulário em branco 
        form = Entryform()
        
    else: 
        # Dados do método POST inseridos no formulário 
        form = Entryform(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit= False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('topic', args=[topic_id]))
    context = {'topic': topic, 'form': form}
    return render(request, 'estudo_Djangos/new_entry.html', context)

def edit_entry(request, entry_id):
    """Editar as anotações dos tópicos """
    entry = Entry.objects.get(id=entry_id)
    topic= entry.topic
    if request.method != 'POST':
        
        form = Entryform(instance=entry)
        
    else:
        # dadosn submetidos no POST
        form = Entryform(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topic', args= [topic.id]))
        
    context= {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'estudo_Djangos/edit_entry.html', context)

        
                   
    

    
        
    
