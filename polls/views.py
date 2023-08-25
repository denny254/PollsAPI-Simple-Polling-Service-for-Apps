from django.shortcuts import render, get_list_or_404 
from django.http import JsonResponse
from . models import poll 

# Create your views here.

def polls_list(request):
    MAX_OBJECTS = 20
    polls = poll.objects.all() [:MAX_OBJECTS]
    data = {'results': list(polls.values('question', 'created_by_username', 'pub_date'))}
    return JsonResponse(data)



def polls_detail(request, pk):
    found_poll =get_list_or_404(poll, id=pk)

    data = {
        
    'results':{
         "question": found_poll[0].question,
         "created_by": found_poll[0].created_by.username,
         "pud_date": found_poll[0].pud_date
        }
    } 
    return JsonResponse(data)