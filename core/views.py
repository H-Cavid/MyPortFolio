from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from .models import *
from django.core.mail import message, send_mail
from django.urls import reverse

# Create your views here.
class HomeTemplateView(TemplateView):
    template_name='home.html'
    #override get context date method

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)#firs,call super get context data
        context['about']=About.objects.first()
        context['services']=Service.objects.all()
        context['works']=RecentWork.objects.all()
        return context

def send_gmail(request):
    if request.method == "POST":
        name=request.POST.get('name')
        subject=request.POST.get('subject')
        message = request.POST.get('message')
        print(name,subject,message)

        #send an email
        send_mail(
            subject,#subject
            message,#messages
            'pragmatechbuild@gmail.com',#from email
            ['cavid.hasanov2@bk.ru'],#To email
            fail_silently=False,
        )

        # return redirect(reverse('home'))
        # return HttpResponseRedirect(('http://127.0.0.1:8000/'))
        # return redirect()
        return HttpResponse('Mesajınız göndərildi.Yadınızda saxlayınki 30 saniyəden bir mesaj göndərə bilərsiz.Zehmət olmasa əsas səhifəyə qayıdın')
    else:
        return HttpResponse("Invalid request")