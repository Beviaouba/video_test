from django.views.generic import View
from django.shortcuts import redirect,reverse

class Index(View):
    TEMPLATE = 'client/base.html'

    def get(self, request):

        return redirect(reverse('client_video_ex'))