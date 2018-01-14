from django.contrib.auth.models import User, Group
from .models import Question, Choice
from django.shortcuts import render, get_object_or_404
from .form import QuestionForm, ChoiceForm
from django.http import JsonResponse
from django.template.loader import render_to_string
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import DjangoModelPermissions

def question_list(request):
    question = Question.objects.all()
    return render(request, 'question_list.html', {'question_list': question})

def save_question_form(request, form, template_name):
    data = dict()

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            question = Question.objects.all()
            data['html_question_list'] = render_to_string('../templates/includes/partial_question_list.html', {
                'question_list': question
            })
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

@api_view(['PUT'])
@permission_classes((DjangoModelPermissions, ))
def question_create(request):
    queryset = User.objects.none()
    if request.method == 'POST':
        form = QuestionForm(request.POST)
    else:
        form = QuestionForm()
    return save_question_form(request, form, '../templates/includes/partial_question_create.html')

def question_update(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
    else:
        form = QuestionForm(instance=question)
    return save_question_form(request, form, '../templates/includes/partial_question_update.html')

def question_delete(request, pk):
    question = get_object_or_404(Question, pk=pk)
    data = dict()
    if request.method == 'POST':
        question.delete()
        data['form_is_valid'] = True
        question = Question.objects.all()
        data['html_question_list'] = render_to_string('../templates/includes/partial_question_list.html', {
            'question_list': question
        })
    else:
        context = {'question': question}
        data['html_form'] = render_to_string('../templates/includes/partial_question_delete.html', context, request=request)
    return JsonResponse(data)

def choice_list(request):
    choices = Choice.objects.all()
    return render(request, 'choice_list.html', {'choice_list': choices})

def save_choice_form(request, form, template_name):
    data = dict()

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            choices = Choice.objects.all()
            data['html_choice_list'] = render_to_string('../templates/includes/partial_choice_list.html', {
                'choice_list': choices
            })
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)
def choice_create(request):
    if request.method == 'POST':
        form = ChoiceForm(request.POST)
    else:
        form = ChoiceForm()
    return save_choice_form(request, form, '../templates/includes/partial_choice_create.html')

def choice_update(request, pk):
    choice = get_object_or_404(Choice, pk=pk)
    if request.method == 'POST':
        form = ChoiceForm(request.POST, instance=choice)
    else:
        form = ChoiceForm(instance=choice)
    return save_choice_form(request, form, '../templates/includes/partial_choice_update.html')

def choice_delete(request, pk):
    choice = get_object_or_404(Choice, pk=pk)
    data = dict()
    if request.method == 'POST':
        choice.delete()
        data['form_is_valid'] = True
        choices = Choice.objects.all()
        data['html_choice_list'] = render_to_string('../templates/includes/partial_choice_list.html', {
            'choice_list': choices
        })
    else:
        context = {'choice': choice}
        data['html_form'] = render_to_string('../templates/includes/partial_choice_delete.html', context, request=request)
    return JsonResponse(data)