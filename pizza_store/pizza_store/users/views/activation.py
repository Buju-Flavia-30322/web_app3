from django.contrib.sites.models import Site
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render,redirect,reverse,HttpResponse, get_object_or_404
from django.template.loader import get_template
from users.utils.constants import ACTIVATION_AVAILABILITY

from django.utils.decorators import decorator_from_middleware
from users.middlewares.activation_middleware import ActivationMiddleware
from users.models import Activation, AVAILABILITY
from django.utils import timezone

@decorator_from_middleware(ActivationMiddleware)
def reset_token_view(request,token):
    if request.method == 'GET':
        return render(request, 'users/activation/reset_token.html',
                      {'token':token})
    activation = get_object_or_404(Activation, token=token)
    activation.expires_at = timezone.now() + timezone.timedelta(**AVAILABILITY)
    activation.save(activation.user)

    return HttpResponse(
        'Token has been reset'
        'please follow the instructions received on your email'
        'in order to activate your account.'
    )

def activate_user(request,token):
    pass


def send_activation_email(user):
    domain = Site.objects.get_current().domain
    url = reverse('users:activation:activate',args=(user.activation.token,))
    activation_url = f'{domain}{url}'
    print('activation_url', activation_url)

    context = {
        'first_name' : user.first_name,
        'last_name': user.last_name,
        'activation_url': activation_url,
        'availability': ACTIVATION_AVAILABILITY
    }

    template = get_template('emails/activation.html')
    content = template.render(context)
    mail = EmailMultiAlternatives(
        subject ='Your account has been created!',
        body=content,
        to=[user.email]
    )
    mail.content_subtype='html'
    mail.send()