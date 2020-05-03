from django.contrib.auth import logout
from django.shortcuts import redirect

from news.views import BaseView


class LogoutView(BaseView):

    def get(self, request):
        logout(request)
        return redirect('login')
