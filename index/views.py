from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Subject, Class, Note, Question
from django.urls import reverse
from random import shuffle

@login_required(login_url='login')
def home(request):
    """
    homepage (no chapter or section)
    """

    context = {}

    return render(request, 'home.html', context)


@login_required(login_url='login')
def subjects(request):
    """
    homepage (no chapter or section)
    """

    subjects = Subject.objects.filter(active=True, author=request.user)

    context = {"subjects": subjects}

    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")

        if title and description:
            Subject.objects.create(
                title=title,
                description=description,
                active=True,
                author=request.user,
            )

            return redirect('subject')

    return render(request, 'classes.html', context)

@login_required(login_url='login')
def classes(request, pk):
    """
    homepage (no chapter or section)
    """
    parent_subject = Subject.objects.filter(subject_id=pk).get()
    clas = Class.objects.filter(active=True, parent_subject=parent_subject).all()

    context = {"classes": clas, "subject": parent_subject}

    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")

        if title and description:
            Class.objects.create(
                parent_subject=parent_subject,
                title=title,
                description=description,
                active=True,
                author=request.user,
            )

            url = reverse('subject_detail', kwargs={'pk': parent_subject.subject_id})
            return redirect(url)

    return render(request, 'Subjects.html', context)

@login_required(login_url='login')
def class_detail(request, pk):
    """
    homepage (no chapter or section)
    """

    clas = Class.objects.filter(active=True, subject_id=pk).get()
    parent_subject = clas.parent_subject
    notes = Note.objects.filter(parent_class=clas)

    context = {"class": clas, "subject": parent_subject, "notes": notes}

    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("content")

        if title and description:
            Note.objects.create(
                parent_class=clas,
                title=title,
                content=description,
                active=True,
                author=request.user,
            )

            url = reverse('class_detail', kwargs={'pk': clas.subject_id})
            return redirect(url)

    return render(request, 'class_detail.html', context)

@login_required(login_url='login')
def notes(request):
    """
    homepage (no chapter or section)
    """

    notes = Note.objects.filter(author=request.user)

    context = {"notes": notes}

    return render(request, 'all_notes.html', context)


@login_required(login_url='login')
def tests(request):
    """
    homepage (no chapter or section)
    """
    context = {}

    return render(request, 'tests.html', context)


@login_required(login_url='login')
def test_create(request, test_type):
    """
    homepage (no chapter or section)
    """

    notes = Note.objects.filter(author=request.user)
    context = {"type": test_type, "notes": notes}

    if request.method == "POST":

        for index, note in enumerate(notes):
            is_included = request.POST.get(f"test{index + 1}") == 'on'
            note.test = is_included
            note.save()


        url = reverse('test', kwargs={'test_type': test_type})
        return redirect(url)

    return render(request, 'create_test.html', context)


@login_required(login_url='login')
def test(request, test_type):
    """
    homepage (no chapter or section)
    """

    notes = Note.objects.filter(author=request.user, test=True)
    questions = []   

    for note in notes:
        questions += Question.objects.filter(parent_note=note)

    shuffle(questions)

    # questions = questions.objects.filter(parent_note=)

    context = {"type": test_type, "notes": notes, "questions": questions}

    if test_type == 'flash_cards':
        return render(request, 'flash_cards.html', context)
    
    if test_type == 'practice_test':
        return render(request, 'practice_test.html', context)
    
    if test_type == 'test':
        return render(request, 'test.html', context)



@login_required(login_url='login')
def note_detail(request, pk):
    """
    homepage (no chapter or section)
    """

    note = Note.objects.filter(active=True, subject_id=pk).get()
    questions = Question.objects.filter(active=True, parent_note=note)
    parent_class = note.parent_class

    context = {"class": parent_class,"note": note, "questions": questions}

    if request.method == "POST":
        if 'update_note' in request.POST:
            new_title = request.POST.get("title")
            new_content = request.POST.get("content")

            if new_title and new_content:
                note.title = new_title
                note.content = new_content
                note.save()
        elif 'update_question' in request.POST:

            for question_id in questions:

                if f'{question_id.subject_id}' in request.POST:

                    question = request.POST.get("question")
                    answer = request.POST.get("answer")
                    case = request.POST.get("case") == 'on'
                    diacritics = request.POST.get("dia") == 'on'
                    symbols = request.POST.get("sym") == 'on'
                    mashed = request.POST.get("mashed") == 'on'

                    if question and answer:
                        question_id.title = question
                        question_id.answer = answer
                        question_id.symbol_strict = symbols
                        question_id.case_strict = case
                        question_id.diacritic_strict = diacritics
                        question_id.can_be_mashed = mashed
                        question_id.save()
            
        else:
            question = request.POST.get("question")
            answer = request.POST.get("answer")
            case = request.POST.get("case") == 'on'
            diacritics = request.POST.get("dia") == 'on'
            symbols = request.POST.get("sym") == 'on'
            mashed = request.POST.get("mashed") == 'on'

            if question and answer:
                Question.objects.create(
                    parent_note=note,
                    title=question,
                    answer=answer,
                    active=True,
                    author=request.user,
                    case_strict=case,
                    diacritic_strict=diacritics,
                    symbol_strict=symbols,
                    can_be_mashed=mashed,
                )

                url = reverse('note_detail', kwargs={'pk': note.subject_id})
                return redirect(url)

    return render(request, 'note_detail.html', context)


#DELETE


@login_required(login_url='login')
def deleteSubject(request, pk):

    subject = Subject.objects.get(subject_id=pk)
    subject.delete()

    return redirect("subject")

@login_required(login_url='login')
def deleteClass(request, pk):

    subject = Class.objects.get(subject_id=pk)
    subject.delete()

    parent_subject = subject.parent_subject

    url = reverse('subject_detail', kwargs={'pk': parent_subject.subject_id})

    return redirect(url)

@login_required(login_url='login')
def deleteNote(request, pk):

    subject = Note.objects.get(subject_id=pk)
    subject.delete()

    parent_subject = subject.parent_class

    url = reverse('class_detail', kwargs={'pk': parent_subject.subject_id})

    return redirect(url)

@login_required(login_url='login')
def deleteQuestion(request, pk):

    subject = Question.objects.get(subject_id=pk)
    subject.delete()

    parent_subject = subject.parent_note

    url = reverse('note_detail', kwargs={'pk': parent_subject.subject_id})

    return redirect(url)

# AUTH


def login_user(request):
    """
    user will log-in here
    """

    context = {}

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, username=User.objects.filter(email=email).get(), password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            context = {"warning": "Password or email are incorrect"}

    return render(request, 'login.html', context)


def logout_user(request):
    """
    log-out function
    """

    logout(request)

    return redirect('login')
