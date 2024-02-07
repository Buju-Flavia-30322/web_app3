from django.urls import path, include
from users.views.activation import activate_user
from users.views.activation import reset_token_view

app_name = 'activation'

urlpatterns = [
    path('activate/', activate_user, name='activate'),
    path('reset_token/', reset_token_view, name='reset_token')

]