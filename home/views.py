from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import random 
from django.http import JsonResponse



def get_quiz(request):
    try:
        question_objs=list(Question.objects.all())
        data=[]
        random.shuffle(question_objs)
        for question_obj in question_objs:
            data.append({
                "category" : question_obj.category.category_name,
                "question" : question_obj.question,
                "marks" : question_obj.marks,
                "answers":  question_obj.get_answers()
            })

            payload = {'starus':True, 'data':data}
            return JsonResponse({})
    except Exception as e:
        print(e)
        return HttpResponse("Something went wrong!")