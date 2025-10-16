from django.db import models
from django.contrib.auth.views import LoginView

class MyLogin(LoginView):
    redirect_authenticated_user = True

    def form_invalid(self, form):
            messages.error(self.request,'Invalid username or password')
            return self.render_to_response(self.get_context_data(form=form))