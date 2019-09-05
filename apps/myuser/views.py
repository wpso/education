# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.backends import ModelBackend
from .models import UserProfile
from django.db.models import Q

from django.views.generic import View
from forms import LoginForm

from django.http import HttpResponse

from .tasks import send_register_email


def index(request):
    send_register_email.delay()
    return HttpResponse(u"邮件发送成功， 请查收")


# Create your views here.

class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            print e
            return None


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user=user)
                return HttpResponseRedirect(reverse('index'))
            return render(request, 'login.html', {'msg': '用户名或密码错误。'})
        else:
            return render(request, 'login.html', {'login_form': login_form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('index'))
