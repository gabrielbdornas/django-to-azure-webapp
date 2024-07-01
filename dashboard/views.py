from django.shortcuts import render

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Question

@login_required
def sinhala_translator_dashboard(request):
    questions = Question.objects.all()
    return render(request, 'dashboard/sinhala_translator_dashboard.html', {'questions': questions})



from django.contrib.auth.decorators import login_required
from .models import Question

@login_required
def tamil_translator_dashboard(request):
    questions = Question.objects.all()
    return render(request, 'dashboard/tamil_translator_dashboard.html', {'questions': questions})


from django.shortcuts import render, get_object_or_404, redirect
from .models import Question

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Question

from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Question

from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Question

def sinhala_editing_interface(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'save':
            question.sinhala_question = request.POST['sinhala_question']
            question.sinhala_answer1 = request.POST['sinhala_answer1']
            question.sinhala_answer2 = request.POST['sinhala_answer2']
            question.sinhala_answer3 = request.POST['sinhala_answer3']
            question.sinhala_v_text = request.POST['sinhala_v_text']
            question.sinhala_a_text = request.POST['sinhala_a_text']
            question.sinhala_k_text = request.POST['sinhala_k_text']
            question.save()
            messages.success(request, 'Edits saved successfully.')
        elif action == 'complete':
            question.sinhala_question = request.POST['sinhala_question']
            question.sinhala_answer1 = request.POST['sinhala_answer1']
            question.sinhala_answer2 = request.POST['sinhala_answer2']
            question.sinhala_answer3 = request.POST['sinhala_answer3']
            question.sinhala_v_text = request.POST['sinhala_v_text']
            question.sinhala_a_text = request.POST['sinhala_a_text']
            question.sinhala_k_text = request.POST['sinhala_k_text']
            question.sinhala_status = 'complete'
            question.save()
            messages.success(request, 'Question marked as complete.')

        return redirect('sinhala_editing_interface', question_id=question.id)  # Redirect to dashboard

    return render(request, 'dashboard/sinhala_editing_interface.html', {'question': question})


def tamil_editing_interface(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'save':
            question.tamil_question = request.POST['tamil_question']
            question.tamil_answer1 = request.POST['tamil_answer1']
            question.tamil_answer2 = request.POST['tamil_answer2']
            question.tamil_answer3 = request.POST['tamil_answer3']
            question.tamil_v_text = request.POST['tamil_v_text']
            question.tamil_a_text = request.POST['tamil_a_text']
            question.tamil_k_text = request.POST['tamil_k_text']
            question.save()
            messages.success(request, 'Edits saved successfully.')
        elif action == 'complete':
            question.tamil_question = request.POST['tamil_question']
            question.tamil_answer1 = request.POST['tamil_answer1']
            question.tamil_answer2 = request.POST['tamil_answer2']
            question.tamil_answer3 = request.POST['tamil_answer3']
            question.tamil_v_text = request.POST['tamil_v_text']
            question.tamil_a_text = request.POST['tamil_a_text']
            question.tamil_k_text = request.POST['tamil_k_text']
            question.tamil_status = 'complete'
            question.save()
            messages.success(request, 'Question marked as complete.')

        return redirect('tamil_editing_interface', question_id=question.id)

    return render(request, 'dashboard/tamil_editing_interface.html', {'question': question})


@login_required
def illustrator_dashboard(request):
    questions = Question.objects.all()
    return render(request, 'dashboard/illustrator_dashboard.html', {'questions': questions})

@login_required
def illustrator_editing_interface(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'save':
            question.question_image_illustration = request.FILES.get('question_image_illustration', question.question_image_illustration)
            question.answer1_image_illustration = request.FILES.get('answer1_image_illustration', question.answer1_image_illustration)
            question.answer2_image_illustration = request.FILES.get('answer2_image_illustration', question.answer2_image_illustration)
            question.answer3_image_illustration = request.FILES.get('answer3_image_illustration', question.answer3_image_illustration)
            question.visual_instructions_illustration = request.FILES.get('visual_instructions_illustration', question.visual_instructions_illustration)
            question.save()
            messages.success(request, 'Illustrations saved successfully.')
        elif action == 'complete':
            question.question_image_illustration = request.FILES.get('question_image_illustration', question.question_image_illustration)
            question.answer1_image_illustration = request.FILES.get('answer1_image_illustration', question.answer1_image_illustration)
            question.answer2_image_illustration = request.FILES.get('answer2_image_illustration', question.answer2_image_illustration)
            question.answer3_image_illustration = request.FILES.get('answer3_image_illustration', question.answer3_image_illustration)
            question.visual_instructions_illustration = request.FILES.get('visual_instructions_illustration', question.visual_instructions_illustration)
            question.illustrator_status = 'complete'
            question.save()
            messages.success(request, 'Illustrations marked as complete.')

        return redirect('illustrator_editing_interface', question_id=question.id)

    return render(request, 'dashboard/illustrator_editing_interface.html', {'question': question})


from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Question
import json

@require_POST
def delete_image(request):
    data = json.loads(request.body)
    question_id = data.get('question_id')
    field = data.get('field')
    question = get_object_or_404(Question, id=question_id)
    
    if field and hasattr(question, field):
        setattr(question, field, None)
        question.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failure'}, status=400)
