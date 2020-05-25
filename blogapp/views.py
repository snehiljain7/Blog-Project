from django.shortcuts import render
from blogapp.models import Blog
from blogapp.forms import BlogForm, SignUpForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail
from django.views.generic import View, TemplateView, CreateView, ListView, DetailView, DeleteView, UpdateView
from django.urls import reverse
# Create your views here.
class Home(View):
    def get(self, request):
        return render(request, 'blogapp/home.html')


class ViewBlog(ListView):
    model = Blog

#@login_required
class DetailBlog(DetailView):
    model = Blog

class AddBlog(CreateView):
    model = Blog
    fields = '__all__'
    def get_success_url(self):
        return reverse('home')

class UpdateBlog(UpdateView):
    model = Blog
    fields = '__all__'
    def get_success_url(self):
        return reverse('home')

class DeleteBlog(DeleteView):
    model = Blog
    def get_success_url(self):
        return reverse('home')
def deleteblog(request, pid):
    images = Blog.objects.get(id = pid)
    images.delete()
    images = Blog.objects.all().order_by('-upload_date')
    mydict = {'images': images}
    return render(request, 'blogapp/viewblog.html', {'images': images})

def SignUp(request):
    signupform = SignUpForm()
    mydict = dict()
    if request.method == 'POST':
        signupform = SignUpForm(request.POST)
        if signupform.is_valid():
            user = signupform.save()
            user.set_password(user.password)
            user.save()
            subject = "Welcome to the Blog Site"
            message = "Welcome "+user.first_name+", You have registered successfully"
            recipient_list = [user.email]
            email_from = settings.EMAIL_HOST_USER
            send_mail (subject, message, email_from, recipient_list)
            mydict.update({'msg': 'Registered successfully'})
    mydict.update({'signupform': signupform})
    return render(request, 'blogapp/signup.html', context = mydict)
