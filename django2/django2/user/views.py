from django.shortcuts import render
from django.views.generic import FormView
from .forms import RegisterForm, LoginForm


def index(request):
    return render(request, 'index.html', {'email': request.session.get('user')})


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm

    # 폼에 정상적인 값이 들어왔을 때
    success_url = '/'


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'

    # 유효성 검사가 끝나고 모든 데이터가 정상적으로 들어와 로그인이 되었을 때
    def form_valid(self, form):
        self.request.session['user'] = form.email
        return super().form_valid(form)
