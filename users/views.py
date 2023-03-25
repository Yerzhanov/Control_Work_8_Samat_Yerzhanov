from django.urls import reverse_lazy, reverse
from django.shortcuts import HttpResponseRedirect
from django.views.generic.base import TemplateView
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from users.models import User, EmailVerification
from django.contrib.messages.views import SuccessMessageMixin
from common.views import TitleMixin


class UserLoginView(TitleMixin, LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    title = 'Магазин - Авторизация'


class UserRegistrationView(TitleMixin, SuccessMessageMixin, CreateView):
    model = User
    form_class =UserRegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Добро пожаловать, вы успешно зарегистрированы!'
    title = 'Магазин - Регистрация пользователя'


class UserProfileView(TitleMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    success_url = reverse_lazy('users:profile')
    title = 'Магазин - Личный кабинет'

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data()
        return context


class EmailVerificationView(TitleMixin, TemplateView):
    title = "Магазин - Подтверждение электронной почты"
    template_name = 'users/email_verification.html'

    def get(self, request, *args, **kwargs):
        code = kwargs['code']
        user = User.objects.get(email=kwargs['email'])
        email_verifications = EmailVerification.objects.filter(user=user, code=code)
        if email_verifications.exists() and not email_verifications.first().is_expired():
            user.is_verified_email = True
            user.save()
            return super(EmailVerificationView, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('index'))

