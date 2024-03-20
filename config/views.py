from django.shortcuts import render
from projects.models import Project
from contactus.models import Footer, Ticket

def home(request):
    if request.method == "POST":
        n = request.POST.get('name')
        e = request.POST.get('mail')
        p = request.POST.get('phone')
        s = request.POST.get('subject')
        t = request.POST.get('text')
        if n and e and s and t:
            Ticket.objects.create(
                name = n, mail = e, subject = s, text = t, phone = p
            )

    projects = Project.objects.all()
    footer = Footer.objects.all().last()
    return render(request, 'index.html', context={'projects' : projects, 'footer': footer})


