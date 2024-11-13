import copy

from django.core.paginator import Paginator
from django.shortcuts import render

from .logic.pagination import paginations_params

QUESTIONS = [
    {
        "title": "title" + str(i),
        "id": str(i),
        "text": 'Culpa ut qui exercitation aute sit eiusmod ullamco excepteur fugiat. \n Est eu id eiusmod officia irure pariatur quis ut consequat enim magna exercitation.' + str(i),
        "comments_count": (2),
    } for i in range(30)
]

MEMBERS = [
    {
        "memberName": f'member {i}'
    } for i in range(5)
]

QUESTIONSHOTLIST = copy.deepcopy(QUESTIONS)
QUESTIONSHOTLIST.reverse()

def Login(request):
    return render(request,
                  'Login.html',
                  context={'questions': QUESTIONS,
                           'members': MEMBERS})

def Register(request):
    return render(request,
                  'Register.html',
                  context={'questions': QUESTIONS,
                           'members': MEMBERS})

def Settings(request):
    return render(request,
                  'Settings.html',
                  context={'questions': QUESTIONS,
                           'members': MEMBERS})

def QuestionsList(request):

    page_num = int(request.GET.get('page', 1))
    paginator = Paginator(QUESTIONS, 5)
    page = paginator.page(page_num)

    params = paginations_params(page_num, paginator, page)
    return render(request,
                  'QuestionsList.html',
                  context={'questions': page.object_list,
                           'page_obj': page,
                           'paginator': paginator,
                           'params': params,
                           'members': MEMBERS
                           }
                  )

def QuestionSingle(request, question_id):
    answers = [
        {
            "title": "title" + str(i),
            "id": str(i),
            "text": 'Quis irure cupidatat ad laborum et et ullamco labore officia voluptate ad. \n Laborum voluptate ea cupidatat dolor officia.' + str(i),
        } for i in range(10)
    ]

    page_num = int(request.GET.get('page', 1))
    paginator = Paginator(answers, 2)
    page_obj = paginator.page(page_num)
    params = paginations_params(page_num, paginator, page_obj)

    return render(request,
                  'QuestionSingle.html',
                  context={'question': QUESTIONS[question_id],
                           'members': MEMBERS,
                           'answers': page_obj.object_list,
                           'page_obj': page_obj,
                           'paginator': paginator,
                           'params': params})

def TagsList(request, tag_name):
    taggedQuestions = [
        {
            "title": "title" + str(i),
            "id": str(i),
            "text": 'Quis irure cupidatat ad laborum et et ullamco labore officia voluptate ad. \n Laborum voluptate ea cupidatat dolor officia.' + str(i),
            "comments_count": (2),
        } for i in range(5)
    ]
    return render(request,
                  'TagsList.html',
                  context={'questions': QUESTIONS,
                           'members': MEMBERS,
                           'taggedQuestions': taggedQuestions,
                           'tag_name': tag_name})

def AddQuestion(request):
    return render(request,
                  'AddQuestion.html',
                  context={'questions': QUESTIONS,
                           'members': MEMBERS})

def QuestionsHot(request):
    page_num = int(request.GET.get('page', 1))
    paginator = Paginator(QUESTIONSHOTLIST, 5)
    page = paginator.page(page_num)


    params = paginations_params(page_num, paginator, page)
    return render(request,
                  'QuestionsHot.html',
                  context={'questions': page.object_list,
                           'page_obj': page,
                           'paginator': paginator,
                           'params': params,
                           'members': MEMBERS}
                  )
