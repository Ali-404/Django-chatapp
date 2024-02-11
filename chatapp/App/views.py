from django.shortcuts import render,redirect
from django.core.serializers import serialize

from django.contrib.auth import login,authenticate,logout,password_validation
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

from django.http import HttpResponse,JsonResponse

import json

from .models import Room,Message





def main(request):
    if (request.user.is_authenticated):
        return redirect("lobby/")
    else:
        return redirect("auth/login")


def LoginView(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        

        user = authenticate(request,username=username, password=password)
        
        if (user is None):
            return redirect(f'../../auth/login/?msg={"Wrong Username or Password!"}&msgtype={"danger"}')
            
        
        login(request,user)
        return redirect(f"../../lobby/?msg={'Logged In Successfully.'}&msgtype={'success'}")
    
    
    if request.user.is_authenticated:
        return redirect("../../lobby/")
        
    
    return render(request, "auth/login.html")


def RegisterView(request):
    
    if (request.method == 'POST'):
        username = request.POST['username']
        gmail = request.POST['gmail']
        password = request.POST['password']
        re_password = request.POST['re_password']

        if (len(User.objects.filter(username=username)) > 0):
            return redirect(f'../register/?msg={"Username already exists! try another one."}&msgtype={"danger"}')
        
        if len(User.objects.filter(email=gmail)) > 0:
            return redirect(f'../register/?msg={"Gmail already used! try another one."}&msgtype={"danger"}')
 
        
        try: 
            password_validation.validate_password(password=password)
        except:
            return redirect(f'../register/?msg={"Password not valid! try anoter one."}&msgtype={"danger"}')
            
        
        if (password != re_password):
            return redirect(f'../register/?msg={"Password not confermed! try again."}&msgtype={"danger"}')
        
        try:
            newUser = User(username=username, email=gmail)
            newUser.set_password(password)
            newUser.save()
            print("New account has been created successfully ! #" + str(newUser))
            return redirect(f"../../lobby/")
        except:
            return redirect(f'../register/?msg={"Unable to create account! try again."}&msgtype={"danger"}')
            
            
    return render(request, "auth/register.html")



def lobby(request):
    if (request.user.is_authenticated):
        return render(request,"lobby.html")
    else:
        return redirect(f'../auth/login/?msg={"Please Log In or Create account First."}&msgtype={"warning   "}')
    
    
    
def ChatView(request,room):
    if (request.method == 'GET'):
        
        theRoom = Room.objects.get(id=room)
        return render(request, 'chat.html', {
            "room":theRoom,
            "messages":serialize('json',Message.objects.filter(room=theRoom))
            
        }) 
    try:
        theRoom = Room.objects.get(id=room)
        return render(request, 'chat.html', {
            "room":theRoom,
            "messages":serialize('json',Message.objects.filter(room=theRoom))
            
        })
    except:
        return redirect(f"../../lobby/?msg={'An Error has  occurred!'}&msgtype={'danger'}")

def CreateRoom(request):
    if request.method == 'POST':
        roomName = request.POST['room_name']
        roomPassword = request.POST['room_password']
        
        if len(Room.objects.filter(name=roomName)) > 0:
            return redirect(f"../lobby/?msg={'Room Name Already Used! Try Another One.'}&msgtype={'danger'}")
        
        try:
            newRoom = Room(name=roomName, password=roomPassword, owner=request.user)
            newRoom.save()

            return redirect(f"../chat/{newRoom.id}") 
        except:
            return redirect(f"../lobby/?msg={'Unable To Create Room. Try Again Later !'}&msgtype={'danger'}") 
        
    return redirect("../lobby/")
        
        

def JoinRoom(request):
    if (request.method == 'POST'):
        room_name = request.POST['room_name']
        # room_password = request.POST['room_password']
        
        try: 
            room = Room.objects.get(name=room_name)
            
            # if (room.password != room_password):
            #     return redirect(f"../lobby/?msg={'Room password is incorrect!'}&msgtype={'danger'}")
            
            return redirect(f"../chat/{room.id}")
        
        except:
            return redirect(f"../lobby/?msg={'Room is not exists!'}&msgtype={'danger'}")

        
    
    return redirect("../lobby/")
    
    
def Logout(request):
    if (request.user.is_authenticated):
        logout(request) 
    return redirect(f'../?msg={"You are logged out."}&msgtype={"info"}')

def SendMessage(request, room):
    if request.method == 'POST':
        message = request.POST["message"]
        sender = request.user

        try:
            theRoom = Room.objects.get(id=room)
            NewMessage = Message(user=sender, room=theRoom, content=message,sender_name=sender.get_username())
            NewMessage.save()

            return redirect(f"../../chat/{room}")
        except:
            return redirect(f'../../lobby/?msg={"Unable to send messages Try Again Later !"}&msgtype={"danger"}' )

    return redirect("../lobby/")



def GetMessages(request):
    # try:
        room = Room.objects.get(id=request.GET['room']) 
        all_messages = Message.objects.filter(room=room).all()
        qs_json = serialize('json', all_messages)
        return HttpResponse(json.dumps({"messages": qs_json}), content_type='application/json')
    # except:
        # return HttpResponse("Can't Load Messages")