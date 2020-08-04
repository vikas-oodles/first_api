from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserForm, ProfileForm, AddressForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import reverse,redirect

#authentication using rest_framework
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
# from rest_framework import generics

from rest_framework import status
from django.contrib.auth.models import User
# from .serializers import ProfileSerializer
from .models import Profile,Address

# Create your views here.
class ProfileView(APIView):
    def get(self, request, username=None):
        if username!=None:
            username = [user.username for user in User.objects.filter(username__startswith=username)]
            return Response(username)

class ProfileDetail(APIView):
    def get(self,request):
        username = [user.username for user in User.objects.all()]
        return Response(username)


#help from https://coderwall.com/p/sll1kw/django-auth-class-based-views-login-and-logout

from django.utils.http import is_safe_url
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import FormView, RedirectView, TemplateView
from django.urls import reverse_lazy

# class ExampleView(APIView):
#     authentication_classes = [SessionAuthentication,BasicAuthentication]
#     permission_classes = [IsAuthenticated]
#
#     def get(self, request, format=None):
#         content = {
#         'user': unicode(request.user),
#         'auth': unicode(request.auth),
#         }
#         return Response(content)

class Index(TemplateView):
    template_name = 'myapp/index.html'

class LoginView(FormView):
    success_url = '/auth/home'
    form_class = AuthenticationForm
    redirect_field_name = REDIRECT_FIELD_NAME

    @method_decorator(sensitive_post_parameters('password'))
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)

    def dispatch(self,request,*args,**kwargs):
        request.session.set_test_cookie()
        return super(LoginView, self).dispatch(request,*args,**kwargs)

    def form_valid(self,form):
        auth_login(self.request,form.get_user())
        return super(LoginView, self).form_valid(form)

    def get_success_url(self):
        # redirect_to = self.redirect_field_name
        # if not is_safe_url(redirect_to,self.request.get_host()):
        #     redirect_to = self.success_url
        return reverse_lazy('home')

class LogoutView(RedirectView):
    url = '/user_login'
    def get(self,request,*args,**kwargs):
        auth_logout(request)
        return super(LogoutView,self).get(request,*args,**kwargs)

# def register(request):
#     registered = False
#
#     userform = UserForm()
#     profileform = ProfileForm()
#
#     if request.method=='POST':
#         userform = UserForm(request.POST)
#         profileform = ProfileForm(request.POST)
#
#         if userform.is_valid() and profileform.is_valid():
#
#             user = userform.save()
#             user.set_password(user.password)
#             user.save()
#             profile = profileform.save(commit=False)
#             profile.user=user
#             if 'profile_pic' in request.FILES:
#                 profile.profile_pic=request.FILES['profile_pic']
#
#             profile.save()
#             registered = True
#     return render(request,'myapp/index.html',{'registered':registered,'userform':UserForm,'profileform':ProfileForm})
#
# def user_login(request):
#     loginform = LoginForm()
#
#     if request.method=='POST':
#         loginform = LoginForm(request.POST)
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(username=username,password=password)
#         if user and user.is_active:
#             login(request,user)
#             return redirect('home')
#         else:
#             return HttpResponseRedirect(reverse('user_login'))
#     else:
#         return render(request,'myapp/login.html',{'loginform':loginform})
#
# @login_required
# def user_logout(request):
#     logout(request)
