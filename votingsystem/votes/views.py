from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Option
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url="/login/")
def index(request):
    questions = Question.objects.all()
    return render(request, "index.html", {"questions": questions})


@login_required
def detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    options = Option.objects.filter(question=question)
    if request.user not in question.voters.all():
        if request.method == "POST":
            try:
                option_chosen = question.option_set.get(
                    pk=request.POST['option'])
            except Option.DoesNotExist:
                return render(request, 'detail.html', {
                    'question': question,
                    "options": options,
                    'error_message': "You didn't select a choice.",
                })
            else:
                option_chosen.votes += 1
                question.voters.add(request.user)
                question.save()
                option_chosen.save()
                if Question.objects.filter(id=question.id+1).exists():
                    return redirect('/{}/'.format(question.id+1))
                else:
                    return redirect('/index/')
    else:
        return render(request, 'results.html', {"question": question, "options": options})

    return render(request, "detail.html", {"question": question, "options": options})


def result(request, pk):
    question = get_object_or_404(Question, pk=pk)
    options = Option.objects.filter(question=question)

    return render(request, 'results.html', {"question": question, "options": options})
