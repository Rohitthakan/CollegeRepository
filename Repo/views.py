from django.shortcuts import render, redirect
from Repo.models import Question, Contact
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

# Create your views here.
def index(request):
    return render(request, 'index.html')

def resources(request):
    br = request.POST.get('branch')
    sem = request.POST.get('semester')
    type_exam = request.POST.get('exam_type')
    if br and sem:
        documents = Question.objects.filter(branch = br, semester = sem, exam_type=type_exam)
    else:
        documents = Question.objects.order_by('-time')[:7]
    context = {'document' : documents}
    return render(request, 'resources.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        contactmsg = EmailMessage(desc, email, to=['collegerepo2023@gmail.com'])
        contactmsg.send()
        ins = Contact(name=name, email=email, phone=phone, desc=desc)
        ins.save()
    return render(request, 'contact.html')
def add(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        branch = request.POST.get("branch")
        semester = request.POST.get("semester")
        subject = request.POST.get("subject")
        exam_type = request.POST.get("exam_type")
        document = request.FILES.get("document")
        # html_message = render_to_string('mail.html', {'data': request.POST})
        # emailmsg = EmailMessage("Subject of the email", html_message, email, to=['collegerepo2023@gmail.com'])
        # emailmsg.content_subtype = "html"
        # emailmsg.send()
        ins = Question(email=email, branch=branch, semester=semester, subject=subject, exam_type=exam_type, document=document)
        ins.save()
        token = ins.token
        html_message = render_to_string('mail.html', {'data': request.POST, 'token': token})
        emailmsg = EmailMessage("Subject of the email", html_message, email, to=['rohitthakan2001@gmail.com'])
        emailmsg.content_subtype = "html"
        emailmsg.send()
    return render(request, 'add.html')

def confirm(request, token):
    submission = Question.objects.get(token=token)
    submission.is_confirmed = True
    submission.save()
    return redirect('success')

def delete(request, token):
    Question.objects.filter(token=token).delete()
    return redirect('deleted')