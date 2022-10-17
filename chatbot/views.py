from django.views.generic import FormView
from .forms import ChatBotForm
from chatbot.functions.Chatbot.Chatbot import *
from django.http import HttpResponse

class ChatBotView(FormView):    
    template_name = 'chatbot.html'
    form_class = ChatBotForm
    success_url = '/'
    
    
    def get(self, request, *args, **kwargs):
        """Handle GET requests: instantiate a blank version of the form."""
        msg = request.GET.get('message')
        print(msg)
        res=chat(msg)
        
        if res == None:
            return self.render_to_response(self.get_context_data())
        else:
            return HttpResponse(res)
   

    
