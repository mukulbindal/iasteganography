from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render

from faker import Faker
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import ChatGrant

from .models import Room

fake = Faker()


def all_rooms(request):
    rooms = Room.objects.all()
    return render(request, 'chat/index.html', {'rooms': rooms})


def room_detail(request, slug):
    room = Room.objects.get(slug=slug)
    return render(request, 'chat/room_detail.html', {'room': room})

# This function will be called by twilio javascript in order to get a unique 
# token so that any end-user can use the chat service using my twilio api-key and 
# account-sid. In Javascript , this funtion will return a json response containing 
# unique token.
def token(request):
    # using below two variables to create a unique identifier of a user-end
    # each user's device-id + his username is always a unique combination
    identity = request.GET.get('identity', request.session['user'])
    device_id = request.GET.get('device', 'default')  # unique device ID
    
    # Below lines just fetch authentication keys from settings
    account_sid = settings.TWILIO_ACCOUNT_SID
    api_key = settings.TWILIO_API_KEY
    api_secret = settings.TWILIO_API_SECRET
    chat_service_sid = settings.TWILIO_CHAT_SERVICE_SID
    
    
    # generate a unique access-token. Identity arguement is used for uniqueness
    # for each individual user.
    token = AccessToken(account_sid, api_key, api_secret, identity=identity)


    # Create a unique endpoint ID for the device
    endpoint = "MyDjangoChatRoom:{0}:{1}".format(identity, device_id)

    # finally grant chat permission.
    if chat_service_sid:
        chat_grant = ChatGrant(endpoint_id=endpoint,
                               service_sid=chat_service_sid)
        token.add_grant(chat_grant)

    response = {
        'identity': identity,
        'token': token.to_jwt().decode('utf-8')
    }
    
    return JsonResponse(response)
def tokenn(request):
    msg = request.GET.get('message')
    print(msg)
    response = {
        'messagefrompython':msg
    }
    
    return JsonResponse(response)